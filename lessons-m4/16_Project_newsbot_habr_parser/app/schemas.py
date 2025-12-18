# Pydantic-схемы
from pydantic import BaseModel, Field, AnyHttpUrl
from datetime import datetime
from uuid import UUID


class NewsItem(BaseModel):
    id: str = Field(
        ...,
        description="uuid новости",
        examples=["asd5aag8as5dg348dfas4"]
    )
    title: str = Field(
        ...,
        min_length=1,
        max_length=300,
        description="Заголовок новсти",
        examples=["Вышла новая версия Python 3.15", "Знакомьтесь с новым фреймворком"]
    )
    url: AnyHttpUrl = Field(
        ...,
        description="Оригинальный url новсти",
        examples=["https://habr.com/ru/articles/12345"]
    )
    summary: str | None = Field(
        default=None,
        description="Короткое описание новсти",
        examples=["Краткий обзор новых функций и изменений Python 3.15"]
    )
    source: str  = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Имя источника",
        examples=["РБК"]
    )
    published_at: datetime  = Field(
        ...,
        description="Время публикации на источнике новости",
        examples=["2025-01-01T00:00:00Z"]
    )
    keywords: list[str] = Field(
        default_factory=list,
        description="Список ключевых слов",
        examples=[["Python", "FastAPI"]]
    )


class PublishedNews(BaseModel):
    news_id: str = Field(
        ...,
        description="uuid новости",
        examples=["asd5aag8as5dg348dfas4"]
    )
    published_at: datetime  = Field(
        ...,
        description="Время публикации в телеграм канале новости",
        examples=["2025-01-01T00:00:00Z"]
    )
    channel_id: str = Field(
        ...,
        description="id телеграм канала",
        examples=["@my_telegram_chanel", "-10001234355466"]
    )


class Keywords(BaseModel):
    id: int = Field(
        ...,
        description="id ключевого слова",
        examples=[1, 2]
    )
    word: str  = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Ключевое слово новости",
        examples=["python", "fastapi"]
    )