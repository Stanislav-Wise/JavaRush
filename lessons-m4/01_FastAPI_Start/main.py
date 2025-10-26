from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from faker import Faker
from random import randint

fake = Faker()


class Movie(BaseModel):
    title: str
    year: int
    description: str


movies = [
    Movie(
        title=fake.company(),
        year=randint(1980, 2025),
        description=fake.paragraph(),
    ),
    Movie(
        title=fake.company(),
        year=randint(1980, 2025),
        description=fake.paragraph(),
    ),
    Movie(
        title=fake.company(),
        year=randint(1980, 2025),
        description=fake.paragraph(),
    ),
    Movie(
        title=fake.company(),
        year=randint(1980, 2025),
        description=fake.paragraph(),
    ),
    Movie(
        title=fake.company(),
        year=randint(1980, 2025),
        description=fake.paragraph(),
    ),
    Movie(
        title=fake.company(),
        year=randint(1980, 2025),
        description=fake.paragraph(),
    )
]

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/about/")
@app.get("/contacts/")
async def about():
    return {"message": "About us"}


@app.get("/movies/", response_model=list[Movie])
async def movie_list():
    """Получить список фильмов."""
    print(f"фильмы - {movies}")
    print(type(movies))
    return movies


@app.get("/movies/{movie_id}/", response_model=Movie)
async def movie_details(movie_id: int):
    """Получаем информацию по фильму."""
    length = len(movies)
    if movie_id > length or movie_id < 0:
        raise HTTPException(status_code=404, detail='Фильм не найден')

    movie_id -= 1
    movie = movies[movie_id]

    print(f" id фильма - {movie_id},фильм  {movie}")
    print(type(movie_id))
    print(type(movie))
    return movie


@app.post("/movies/", response_model=Movie, status_code=201) #
async def movie_create(movie: Movie):
    """Добавить новый фильм."""
    movies.append(movie)
    return movie


#
# @app.get("/movies/{movie_id}/{rating}/{author}/")
# async def movies(movie_id: int, rating: int, author: str):
#     print(f" id фильма - {movie_id}, рейтинг фильма {rating}, автор фильма {author}")
#     print(type(movie_id))
#     print(type(rating))
#     print(type(author))
#     return {"message": f"Movie {movie_id + 100}"}