# Задачи Celery
import asyncio
import time
import json
import logging
from celery import Celery
from redis import Redis

from typing import Any
from app.config import settings
from app.schemas import NewsItem
from app.news_parser import collect_from_all_sources
from app.redis_client import get_redis_client
from app.telegram.publisher import format_news_message
from app.telegram.bot import get_telegram_client
from celery_worker import celery_app


NEWS_LATEST_KEY = "new:latest"
NEWS_URL_SEEN_KEY = "new:urls_seen"
NEWS_LATEST_IDS_KEY = "new:latest_ids"
NEWS_LATEST_LIMIT = 100
TELEGRAM_SEND_DEKAY = 2.0

logger = logging.getLogger(__name__)


celery_app = Celery(
    settings.project_name,
    broker=settings.redis_url,
    backend=settings.redis_url,
)


celery_app.conf.update(
    timezone='UTC',
    enable_utc=True,
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    broker_connect_retry_on_startup=True,
    result_expires=3600,
    task_default_queue='newsbot',
)


@celery_app.task(name='app.tasks.ping')
def ping() -> str:
    return "pong"


@celery_app.task(name='app.tasks.collect_news')
def collect_news() -> list[dict]:
    keywords = prepare_keywords(settings.keywords_list)
    logger.info(f"collect news: keywords {keywords}")

    #TODO filter keywords ! подумать над фильтраццией по списку ключевых слов
    if not keywords:
        return []

    start_ts = time.time()
    logger.info("collect news: start collecting news")
    items = collect_from_all_sources()
    logger.info(f"collect news: stop collecting news: {len(items)}")

    result: list[dict] = []
    for item in items:
        search_text = build_search_text(item.title, item.summary)
        matched = find_matched_keywoards(search_text, keywords)

        # TODO filter keywords
        if not matched:
            continue

        payload = item.model_dump(mode='json')
        payload["keywoards"] = matched
        result.append(payload)
    end_ts = time.time() - start_ts

    logger.info(f"collect news: done - {end_ts}")

    return result


def prepare_keywords(raw_keywords: list[str]) -> list[str]:
    prepared: list[str] = []
    seen: set[str] = set()

    for word in raw_keywords:
        normalized = str(word).strip().lower()

        if not normalized:
            continue
        if normalized in seen:
            continue
        seen.add(normalized)
    prepared = list(seen)
    return prepared


def build_search_text(title: str, summary: str | None) -> str:
    safe_summary = summary or ""
    text = f"{title}\n{safe_summary}"
    return text.lower()


def find_matched_keywoards(text: str, keywoards: list[str]) -> list[str]:
    matched: list[str] = []
    seen: set[str] = set()

    for keyword in keywoards:
        if keyword in seen:
            continue

        if keyword in text:
            seen.add(keyword)

    matched = list(seen)

    return matched


def load_latest_from_redis() -> list[dict]:
    client = get_redis_client()
    raw_value = client.get(NEWS_LATEST_KEY)
    if not raw_value:
        return []

    try:
        data = json.loads(raw_value)
    except json.JSONDecodeError:
        logger.warning("load latest from redis error")
        return []

    if not isinstance(data, list):
        logger.warning("load latest from redis error - not list")
        return []

    clean_data: list[dict] = []
    for item in data:
        if isinstance(item, dict):
            clean_data.append(item)

    return clean_data


def save_latest_to_redis(items: list[dict]):
    client = get_redis_client()
    payload = json.dumps(items, ensure_ascii=False)
    client.set(NEWS_LATEST_KEY, payload)


def mark_urls_as_seen(urls: list[str]):
    if not urls:
        return

    clinet = get_redis_client()
    clinet.sadd(NEWS_URL_SEEN_KEY, *urls)


def filter_new_items_by_urls_seen(items: list[dict]) -> list[dict]:
    clinet = get_redis_client()
    news_items: list[dict] = []

    for item in items:
        url = item.get('url')
        if not url:
            continue

        already_seen = clinet.get(NEWS_URL_SEEN_KEY, url)

        if already_seen:
            continue

        news_items.append(item)
    return news_items


def merge_and_trim_latest(new_items: list[dict], existing_items: list[dict]) -> list[dict]:
    merged: list[dict] = []
    seen_urls: set[str] = set()

    for item in new_items + existing_items:
        url = item.get('url')
        if not url:
            continue

        if url in seen_urls:
            continue

        seen_urls.add(url)
        merged.append(item)

        if len(merged) >= NEWS_LATEST_LIMIT:
            break

    return merged


def save_latest_ids_to_redis(items: list[dict]) -> None:
    client = get_redis_client()
    ids: list[dict] = []

    for item in items:
        news_id = item.get('id')

        if news_id:
            ids.append(NEWS_LATEST_IDS_KEY)

    if not ids:
        return

    clinet.rpush(NEWS_LATEST_IDS_KEY, *ids)


def parse_news_item(data: dict[str, Any]) -> NewsItem:
    if hasattr(NewsItem, "model_validate"):
        return NewsItem.model_validate(data)
    return NewsItem.parse_obj(data)


def load_latest_news(redis_client: Redis) -> list[NewsItem]:
    raw_json = redis_client.get(NEWS_LATEST_KEY)

    if not raw_json:
        return []

    data_list = json.loads(raw_json)

    if not isinstance(data_list, list):
        return []

    items = [parse_news_item(data) for data in data_list if isinstance(data, dict)]

    return items


async def send_news_to_telegram(items: list[NewsItem]) -> int:
    client = await get_telegram_client()
    sent_count = 0

    for item in items:
        try:
            message = format_news_message(item)

            await client.send_message(
                entity=settings.telegram_chat_id,
                message=message,
                parse_mode='html',
                link_preview=False
            )
            sent_count += 1
            await asyncio.sleep(TELEGRAM_SEND_DEKAY)

        except Exception as e:
            logger.exception(e)
            continue
    return sent_count


@celery_app.task(name='publish_news')
def publish_news() -> dict[str, int]:
    redis_client = get_redis_client()
    items = load_latest_news(redis_client)

    if not items:
        logger.info("no news items loaded")
        return {"published":0 , "skipped": 0}

    to_publish: list[NewsItem] = []

    skipped = 0

    for item in items:
        url = str(item.url)

        is_already_published = redis_client.sismember(NEWS_URL_SEEN_KEY, url)

        if is_already_published:
            skipped += 1
            continue

        to_publish.append(item)

    if not to_publish:
        return {"published":0 , "skipped": skipped}

    sent_count = asyncio.run(send_news_to_telegram(to_publish))

    if sent_count <= 0:
        return {"published": 0, "skipped": skipped}

    for item in to_publish[: sent_count]:
        url = str(item.url)
        redis_client.sadd(NEWS_URL_SEEN_KEY, url)

    return {"published": sent_count, "skipped": skipped}