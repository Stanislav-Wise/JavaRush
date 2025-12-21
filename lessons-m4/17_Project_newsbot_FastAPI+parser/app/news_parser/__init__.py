from datetime import datetime
import logging
import hashlib
from typing import Any
from app.schemas import NewsItem
from app.news_parser import habr, rbc


NEWS_SOURCES = [
    'habr',
    'rbc',
]


logger = logging.getLogger(__name__)


def generate_news_id(source: str, url: str) -> str:
    base = f'{source}:{url}'

    digest = hashlib.sha256(base.encode("utf-8")).hexdigest()
    return digest


def normalize_published_at(raw_published_at: str) -> datetime | None:
    if isinstance(raw_published_at, datetime):
        return raw_published_at

    if raw_published_at is None or raw_published_at == '':
        return None

    if isinstance(raw_published_at, str):
        possible_format = [
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%dT%H:%M:%S.%z",
            "%Y-%m-%dT%H:%M:%S.%f",
            "%d.%m.%Y, %H:%M:%S",
        ]
        for fmt in possible_format:
            try:
                return datetime.strptime(raw_published_at, fmt)
            except ValueError:
                continue
        return None
    return None


# def normalize_raw_news(source_name: str, raw_item: dict[str, Any]) -> NewsItem:
#     raw_title = raw_item.get('title', '')
#     title = str(raw_title).strip()
#
#     raw_url = raw_item.get('url') or raw_item.get('link')
#     if not raw_url:
#         raise ValueError(f'Не верный url в {title}')
#
#     url = str(raw_url).strip()
#
#     raw_summary = raw_item.get('summary') or raw_item.get('description') or ''
#     summary = str(raw_summary).strip()
#
#     raw_source = raw_item.get('source') or source_name
#     source = str(raw_source).strip()
#
#     raw_published_at = raw_item.get('published_at') or raw_item.get('date')
#
#
#     published_at = normalize_published_at(raw_published_at)
#
#     #
#     if published_at is None:
#         published_at = datetime.now(timezone.utc)
#
#     news_id = generate_news_id(source=source, url=url)
#
#     keywords = []
#
#     news_item = NewsItem(
#         id=news_id,
#         title=title,
#         url=url,
#         summary=summary,
#         source=source,
#         published_at=published_at,
#         keywords=keywords,
#     )
#     # print (news_item)
#
#     return news_item


def normalize_raw_news(source_name: str, raw_item: dict[str, Any]) -> NewsItem:
    source = source_name
    url = raw_item['url']
    news_id = generate_news_id(source, url)
    news_item = NewsItem(
        id=news_id,
        title=raw_item.get('title'),
        url=raw_item.get('url'),
        summary=raw_item.get('summary') or 'Нет текста',
        source=source,
        published_at=datetime.now(timezone.utc),
        keywords=[],
    )
    # print (news_item)

    return news_item



def collect_from_all_sources() -> list[NewsItem]:
    collected_news: list[NewsItem] = []
    sources = [
        ("habr",  habr.fetch_habr_news_raw),
        # ("rbc",  rbc.fetch_rbc_news_raw),
    ]

    for source, fetch_func in sources:
        try:
            raw_items = fetch_func()
        except Exception as exc:
            # logger.error('Ошибка при парсинге новостей', source, exc)
            logger.error(f'Ошибка при парсинге новостей {source}')
            continue

        for raw_item in raw_items:
            try:
                news_item = normalize_raw_news(source_name=source, raw_item=raw_item)
            except Exception as exc:
                # logger.warning("Не получилось нормализовать новость", source, exc, raw_item)
                logger.warning(f"Не получилось нормализовать новость {raw_item}")
                continue
            collected_news.append(news_item)

    return collected_news

