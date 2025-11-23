from db.session import SessionLocal
from models.genry import Genre
from models.movie import Movie
from models.review import Review


def main():
    session = SessionLocal()

    try:

        print('My genre')

        # WHERE = 'Action'
        my_genre = session.query(Genre).filter_by(name='Company').first()

        if my_genre is None:
            print('Жанр Action не найден.')


        for movie in my_genre.movies:
            print(f'Отзывы {movie.title=} {movie.year=}')
            for review in movie.reviews:
                print(f'--- {review.rating} - {review.text}')

    except Exception as e:
        # Если что-то не так, то откатываемся
        session.rollback()
        raise e

    finally:
        # Закрыть сессию
        session.close()


if __name__ == '__main__':
    main()