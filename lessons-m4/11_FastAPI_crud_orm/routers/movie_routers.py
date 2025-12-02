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
    db: Session = Depends(get_db),
    year: int = Query(None, description="Year of release"),
    title: str = Query(None, description="Movie title"),
):
    """Получить список фильмов."""
    query =  db.query(Movie)

    if year is not None:
        query = query.filter(Movie.year >= year)
    if title is not None:
        query = query.filter(Movie.title.ilike(f'%{title}%'))

    query = query.order_by(Movie.year.desc(), Movie.id.desc())
    all_movies = query.all()
    return all_movies


@router.get("/{movie_id}/", response_model=MoviePublic)
async def movie_details(
    movie_id: int,
    db: Session = Depends(get_db),
):
    """Получаем информацию по фильму."""

    movie = (
        db.query(Movie)
        .filter(Movie.id == movie_id)
        .first()
    )

    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Фильм c {movie_id=} не найден')

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
async def movie_edit(movie_id: int, movie_in: MovieUpdate, db: Session = Depends(get_db)):
    """Изменить фильм."""

    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Фильм c {movie_id=} не найден')

    if movie_in.genre_id is not None:
        genre = db.query(Genre).filter(Genre.id == movie_in.genre_id).first()

        if genre is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Жанр c {movie_in.genre_id=} не найден')

    movie.title = movie_in.title
    movie.year = movie_in.year
    movie.description = movie_in.description
    movie.genre_id = movie_in.genre_id
    db.commit()
    db.refresh(movie)

    return movie



@router.delete("/{movie_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def movie_delete(movie_id: int, db: Session = Depends(get_db)):
    """Удалить фильм."""
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Фильм c {movie_id=} не найден')

    db.delete(movie)
    db.commit()

    return {'message': f'Фильм {movie.title} {movie.year} был успешно удален'}
