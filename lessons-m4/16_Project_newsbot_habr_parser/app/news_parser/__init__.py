from datetime import datetime
import hashlib
from typing import Any
from app.schemas import NewsItem


NEWS_SOURCES = [
    'habr',
    'rbc',
]


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


def normalize_raw_news(source_name: str, raw_item: dict[str, Any]) -> NewsItem:
    raw_title = raw_item.get('title', '')
    title = str(raw_title).strip()

    raw_url = raw_item.get('url') or raw_item.get('link')
    if not raw_url:
        raise ValueError(f'Не верный url в {title}')

    url = str(raw_url).strip()

    raw_summary = raw_item.get('summary') or raw_item.get('description') or ''
    summary = str(raw_summary).strip()

    raw_source = raw_item.get('source') or source_name
    source = str(raw_source).strip()

    raw_published_at = raw_item.get('published_at') or raw_item.get('date')
    published_at = normalize_published_at(raw_published_at)

    news_id = generate_news_id(source=source, url=url)

    keywords = []

    news_item = NewsItem(
        id=news_id,
        title=title,
        url=url,
        summary=summary,
        source=source,
        published_at=published_at,
        keywords=keywords,
    )
    return news_item