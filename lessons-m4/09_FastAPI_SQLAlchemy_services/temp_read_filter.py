from db.session import SessionLocal
from models.genry import Genre
from models.movie import Movie
from models.review import Review


def main():
    session = SessionLocal()

    try:

      # movies = session.query(Movie).all()
      #
      # for movie in movies:
      #     print(f'Film {movie.title=} {movie.year=}')

        # WHERE

        # # filter
        # query = session.query(Movie)
        # query = query.filter((Movie.year > 2000) & (Movie.year < 2010))
        # for movie in query.all():
        #     print(f'Отзывы {movie.title=} {movie.year=}')
        #     print()
        #
        # # filter_by
        # query = session.query(Movie)
        # query = query.filter_by(title='Eye')
        # for movie in query.all():
        #     print(f'Отзывы {movie.title=} {movie.year=}')
        #     print()


        genre = session.query(Genre).first()
        print(genre.name)

    except Exception as e:
        # Если что-то не так, то откатываемся
        session.rollback()
        raise e

    finally:
        # Закрыть сессию
        session.close()


if __name__ == '__main__':
    main()