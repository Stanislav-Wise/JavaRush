from fastapi import  HTTPException,Query, APIRouter
from faker import Faker
from random import randint
from schemas.movie import MovieBase, MovieCreate, MovieUpdate, MovieInDB, MoviePublic

fake = Faker()


movies = [MovieInDB(id=i+1, title=fake.word(), year=randint(1980, 2025),description=fake.paragraph()) for i in range(7)]
# movies = [MovieBase(title=fake.word(), year=randint(1980, 2025),description=fake.paragraph()) for _ in range(0)]

router = APIRouter()


@router.get("/", response_model=list[MoviePublic])
async def movie_list(
    year: int = Query(None, description="Year of release"),
    title: str = Query(None, description="Movie title"),
):
    """Получить список фильмов."""
    result = movies
    if year is not None:
        result = [movie for movie in result if movie.year == year]
    if title is not None:
        result = [movie for movie in result if movie.title.lower() == title.lower()]
    return result


@router.get("/{movie_id}/", response_model=MoviePublic)
async def movie_details(movie_id: int):
    """Получаем информацию по фильму."""
    length = len(movies)
    if movie_id > length or movie_id < 0:
        raise HTTPException(status_code=404, detail='Фильм не найден')

    movie_id -= 1
    movie = movies[movie_id]

    return movie


@router.post("/", response_model=MoviePublic, status_code=201) #
async def movie_create(movie: MovieCreate):
    """Добавить новый фильм."""
    for m in movies:
        if m.title.lower() == movie.title.lower() and m.year == movie.year:
            raise HTTPException(status_code=409, detail='Такой фильм уже есть в базе')
    movies.append(movie)
    return movie


@router.put("/{movie_id}/", response_model=MoviePublic)
async def movie_edit(movie_id: int, movie: MovieUpdate):
    """Изменить фильм."""
    length = len(movies)
    if movie_id > length or movie_id < 0:
        raise HTTPException(status_code=404, detail='Фильм не найден')

    movie_id -= 1
    movies[movie_id].title = movie.title
    movies[movie_id].year = movie.year
    movie = movies[movie_id]

    return movie


@router.delete("/{movie_id}/")
async def movie_delete(movie_id: int):
    """Удалить фильм."""
    length = len(movies)
    if movie_id > length or movie_id < 0:
        raise HTTPException(status_code=404, detail='Фильм не найден')

    movie_id -= 1
    movie = movies.pop(movie_id)

    return {'message': f'Фильм {movie.title} {movie.year} был успешно удален'}
