from sqlalchemy.orm import Session
from models.genry import Genre
from models.movie import Movie
from models.review import Review


def _get_or_create_genre_by_name(session: Session, genre_name: str) -> Genre:
    genre = session.query(Genre).filter_by(name=genre_name).first()

    if genre is not None:
        return genre

    genre = Genre(name=genre_name)

    session.add(genre)
    session.commit()
    session.refresh(genre)

    return genre


def create_movie(
    session: Session,
    title: str,
    year: int,
    description: str | None,
    genre_name: str,
) -> Movie:

    genre = _get_or_create_genre_by_name(session, genre_name)
    movie = Movie(
        title=title,
        year=year,
        description=description,
        genre_id=genre.id,
    )

    session.add(movie)
    session.commit()
    session.refresh(movie)

    return movie


def list_movies(session: Session, year_from: int | None = None, genre_name: str | None = None) -> list[Movie]:
    query = session.query(Movie)

    if year_from is not None:
        query = query.filter(Movie.year >= year_from)

    if genre_name is not None:
        query = query.join(Movie.genre)
        query = query.filter(Genre.name == genre_name)

    query = query.order_by(Movie.year.asc())

    movies = query.all()
    return movies


def get_movie_by_id(session: Session, movie_id: int) -> Movie | None:
    movie = session.query(Movie).filter(Movie.id == movie_id).first()
    return movie