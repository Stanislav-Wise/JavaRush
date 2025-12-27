# Задачи Celery
import time
import logging
from celery import Celery

from app.config import settings
from app.news_parser import collect_from_all_sources

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
    start_ts = time.time()
    logger.info("collect news: start collecting news")
    items = collect_from_all_sources()
    logger.info(f"collect news: stop collecting news: {len(items)}")

    result: list[dict] = []
    for item in items:
        payload = item.model_dump(mode='json')
        result.append(payload)
    end_ts = time.time() - start_ts

    logger.info(f"collect news: done - {end_ts}")

    return result