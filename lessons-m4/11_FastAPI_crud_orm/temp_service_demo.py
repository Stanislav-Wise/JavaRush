from db.session import SessionLocal
from services.movie_service import create_movie, list_movies, get_movie_by_id


def main():
    session = SessionLocal()

    try:
        movie_1 = create_movie(
            session=session,
            title='Matrix',
            year=2001,
            description='Classic action movie',
            genre_name='Classic action',
        )

        movie_2 = create_movie(
            session=session,
            title='Matrix 2',
            year=2005,
            description='Classic action movie 2',
            genre_name='Classic action',
        )
        print(f'Film 1 {movie_1.title=} {movie_1.year=}')
        print(f'Film 2 {movie_2.title=} {movie_2.year=}')

        print()
        print('ВСЕ ФИЛЬМЫ после 2000')
        movies_all = list_movies(session=session, year_from=2000)
        for movie in movies_all:
            print(f'Film  {movie.title=} {movie.year=}')


        print()
        print('ПОИСК ФИЛЬМЫ ')

        movie_id_to_find = movie_2.id
        found_movie = get_movie_by_id(session=session, movie_id=movie_id_to_find)

        if found_movie is not None:
            print(f'Найден Фильм Film  {found_movie.title=} {found_movie.year=}')

    except Exception as e:
        # Если что-то не так, то откатываемся
        session.rollback()
        raise e

    finally:
        # Закрыть сессию
        session.close()


if __name__ == '__main__':
    main()