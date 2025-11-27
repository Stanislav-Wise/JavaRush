from fastapi import  HTTPException, Query, APIRouter, Depends, status
from sqlalchemy.orm import Session
from faker import Faker
from random import randint
from schemas.movie import MovieBase, MovieCreate, MovieUpdate, MovieInDB, MoviePublic
from db.session import SessionLocal, get_db
from models.genry import Genre
from models.movie import Movie
from models.review import Review


fake = Faker()


movies = [MovieInDB(id=i+1, title=fake.word(), year=randint(1980, 2025),description=fake.paragraph()) for i in range(7)]
# movies = [MovieBase(title=fake.word(), year=randint(1980, 2025),description=fake.paragraph()) for _ in range(0)]

router = APIRouter()


@router.get("debug-movies-count")
async def debug_movies_count(db: Session = Depends(get_db)):

    movies_count = db.query(Movie).count()

    return  {'movies_count': movies_count}


@router.get("/", response_model=list[MoviePublic])
async def movie_list(
    year: int = Query(None, description="Year of release"),
    title: str = Query(None, description="Movie title"),
):
    """Получить список фильмов."""
    session = SessionLocal()
    all_movies =  session.query(Movie).all()
    session.close()
    for movie in all_movies:
        print(movie.title)
    result = all_movies
    if year is not None:
        result = [movie for movie in result if movie.year >= year]
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


@router.post("/", response_model=MoviePublic, status_code=status.HTTP_201_CREATED) #
async def movie_create(movie_in: MovieCreate, db: Session = Depends(get_db)):
    """Добавить новый фильм."""
    if movie_in.genre_id is None:
        genre = db.query(Genre).filter(Genre.id == movie_in.genre_id).first()

        if genre is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Жанр с таким id не найден'
            )
    new_movie = Movie(
        title=movie_in.title,
        year=movie_in.year,
        description=movie_in.description,
        genre_id=movie_in.genre_id,

    )

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return new_movie


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
