import random
from faker import Faker

from db.session import SessionLocal, Base, engine
from models.genry import Genre
from models.movie import Movie
from models.review import Review


NUM_GENRES = 5
NUM_MOVIES = 10
NUM_REVIEWS = 5


fake = Faker()
#
# Faker.seed(123)
# random.seed(123)


def reset_table(session):
    session.query(Review).delete()
    session.query(Movie).delete()
    session.query(Genre).delete()
    session.commit()


def create_genres(session) -> list[Genre]:

    genres: list[Genre] = []
    genres_name_set = set()

    while len(genres_name_set) < NUM_GENRES:
        name = fake.word()
        name = name.capitalize()
        genres_name_set.add(name)

    genres_name_list = list(genres_name_set)

    for name in genres_name_list:
        genre = Genre(name=name)
        session.add(genre)
        genres.append(genre)

    session.commit()

    return genres


def create_movies(session, genres: list[Genre]) -> list[Movie]:
    """Создание фильмов."""

    movies: list[Movie] = []

    for genre in genres:
        for _ in range(NUM_MOVIES):
            title = fake.sentence(nb_words=1)
            title = title.strip().rstrip('.').capitalize()

            description = fake.paragraph(nb_sentences=2)
            year = random.randint(1950, 2025)
            movie = Movie(
                title=title,
                year=year,
                description=description,
                genre_id=genre.id,
            )

            session.add(movie)
            movies.append(movie)
    session.commit()
    return movies


def create_rewiews(session, movies: list[Movie]) -> None:
    """Создание отзывов."""

    for movie in movies:

        for _ in range(NUM_REVIEWS):
            rating = random.randint(1, 10)
            text = fake.paragraph(nb_sentences=1)
            review = Review(
                movie_id=movie.id,
                rating=rating,
                text=text,
            )
            session.add(review)
    session.commit()


def main():
    Base.metadata.create_all(engine)

    with SessionLocal() as session:
        reset_table(session)
        genres = create_genres(session)
        movies = create_movies(session, genres)
        create_rewiews(session, movies)

        total_genres = session.query(Genre).count()
        total_movies = session.query(Movie).count()
        total_reviews = session.query(Review).count()

        print(f'Genres: {total_genres}')
        print(f'Movies: {total_movies}')
        print(f'Reviews: {total_reviews}')


if __name__ == '__main__':
    main()



