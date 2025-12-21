""" Маршруты для FastAPI """
from fastapi import APIRouter, HTTPException, status
from app.schemas import NewsItem, PublishedNews, Keywords
from app.news_parser import collect_from_all_sources


api_router = APIRouter()


@api_router.get("/health")
async def health():
    return {"status": "ok"}


@api_router.get("/news", response_model=list[NewsItem])
async def news_list() -> list[NewsItem]:
    fake_news = [
        NewsItem(
            id="test1",
            title="FastAPI 2.0.1 is released",
            url="https://fastapi.tiangolo.com/",
            summary="Короткое описание новости про релиз FastAPI",
            source="FastAPI blog",
            published_at="2025-01-01T00:00:00Z",
            keywords=["python", "fastapi"]
        ),
        NewsItem(
            id="test2",
            title="Python 3.15.1 is released",
            url="https://python.org/",
            summary="Короткое описание новости про релиза python",
            source="Python blog",
            published_at="2025-01-02T00:00:00Z",
            keywords=["python"]
        )
    ]
    return fake_news


@api_router.get("/news/scrape", response_model=list[NewsItem])
async def scrape_news():
    news_items = collect_from_all_sources()
    return news_items