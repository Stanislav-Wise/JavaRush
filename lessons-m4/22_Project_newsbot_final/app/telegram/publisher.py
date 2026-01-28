import html
from app.schemas import NewsItem


TITLE_MAX_LENGTH = 200
SUMMARY_MAX_LENGTH = 700

DEFAULT_SUMMARY = "Читать подробней по url"


def _normalize_text(value: str | None) -> str:
    if value is None:
        return ""

    text = str(value)
    text = text.strip()
    return text


def _truncate_text(text: str, max_len: int) -> str:
    if len(text) <= max_len:
        return text

    return text[:max_len - 3].rstrip() + '...'


def format_news_message(item: NewsItem) -> str:
    title_raw = _normalize_text(item.title)
    title_short = _truncate_text(title_raw, TITLE_MAX_LENGTH)

    source_raw = _normalize_text(item.source)

    summary_raw = _normalize_text(item.summary)
    if not summary_raw:
        summary_raw = DEFAULT_SUMMARY

    summary_short = _truncate_text(summary_raw, SUMMARY_MAX_LENGTH)

    url = str(item.url)

    title_html = html.escape(title_short)
    source_html = html.escape(source_raw)
    summary_html = html.escape(summary_raw)

    message = (
        f'<b>{title_html}</b>\n'
        f'<i>{source_html}</i>\n\n'
        f'{summary_html}\n\n'
        f'<a href="{title_html}">Читать полностью.</a>'
    )

    return message