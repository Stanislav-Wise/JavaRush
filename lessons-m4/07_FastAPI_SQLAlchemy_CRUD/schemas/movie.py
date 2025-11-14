from datetime import date
from pydantic import BaseModel, Field, field_validator


class MovieBase(BaseModel):
    """Модель фильма для нашего API"""
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
        # le=date.today().year,
        description="Год выхода фильма. Обязательно поле. Не менее 1900 и не быть из будущего.",
        examples=[1990, 2010, 2025]

    )
    description: str | None = Field(
        None,
        description="Краткое описание фильма. Не обязательно поле",
        examples=['Фантастический боевик про виртуальную реальность.', 'Детективная драмма с элементами триллера.']
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


class MovieUpdate(MovieBase):
    """Модель для создания фильма."""
    pass


class MoviePublic(MovieBase):
    """Модель для создания фильма."""
    pass


class MovieInDB(MovieBase):
    """Модель для создания фильма."""
    id : int = Field(
        ...,
        description='id фильма в базе.',
        examples=[1, 2, 3]

    )