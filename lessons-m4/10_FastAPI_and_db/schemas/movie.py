from datetime import date
from pydantic import BaseModel, Field, field_validator
from typing import Optional


class MovieBase(BaseModel):
    """Схема фильма для нашего API"""
    title: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Название фильма. Обязательно поле",
        examples=['Matrix', 'Interstellar']
    )
    year: int = Field(
        ...,
        ge=1900,
        le=date.today().year,
        description="Год выхода фильма. Обязательно поле. Не менее 1900 и не быть из будущего.",
        examples=[1990, 2010, 2025]

    )
    description: str | None = Field(  # Optional[str]
        None,
        description="Краткое описание фильма. Не обязательно поле",
        examples=['Фантастический боевик про виртуальную реальность.', 'Детективная драмма с элементами триллера.']
    )

    genre_id: int | None = Field(
        None,
        description='ID жанра (genres.id)',
        examples=[1, 2, 3]
    )

    @field_validator('title')
    @classmethod
    def normalize_title(cls, value: str) -> str:
        clean_value = value.strip()
        if not clean_value:
            raise ValueError('Ваш заголовок фильма состоит из одних пробелов.')
        return clean_value

    @field_validator('year')
    @classmethod
    def check_year(cls, value: int) -> int:
        current_year = date.today().year
        if value > current_year:
            raise ValueError(f'Год фильма должен быть не больше {current_year}.')
        return value


class MovieCreate(MovieBase):
    """Модель для создания фильма."""
    pass


class MovieUpdate(BaseModel):
    """Схема для нашего API"""
    title: Optional[str] = Field(
        None,
        min_length=2,
        max_length=100,
        description="Название фильма. Обязательно поле",
        examples=['Matrix', 'Interstellar']
    )
    year: Optional[int] = Field(
        None,
        ge=1900,
        le=date.today().year,
        description="Год выхода фильма. Обязательно поле. Не менее 1900 и не быть из будущего.",
        examples=[1990, 2010, 2025]

    )
    description: Optional[str] = Field(
        None,
        description="Краткое описание фильма. Не обязательно поле",
        examples=['Фантастический боевик про виртуальную реальность.', 'Детективная драмма с элементами триллера.']
    )

    genre_id: Optional[int] = Field(
        None,
        description='ID жанра (genres.id)',
        examples=[1, 2, 3]
    )



class MovieInDBBase(MovieBase):
    """Схема для создания фильма."""
    id : int = Field(
        ...,
        description='id фильма в базе.',
        examples=[1, 2, 3]
    )

    class Config:
        orm_mode = True
    # movie_scheme = MoviePublic.from_orm(movie_orm_instance)


class MoviePublic(MovieInDBBase):
    """Схема для наружнего представления фильма."""
    pass


class MovieInDB(MovieInDBBase):
    """Cхема для создания фильма."""
    pass