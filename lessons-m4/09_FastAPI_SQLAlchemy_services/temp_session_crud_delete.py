from db.session import SessionLocal
from models.genry import Genre
from models.movie import Movie
from models.review import Review


def main():
    session = SessionLocal()

    try:

        print('Delete genre')

        # WHERE = 'Action'
        genre_to_delete = session.query(Genre).filter_by(name='Комедия').first()

        if genre_to_delete is None:
            print('Жанр не найден.')
            return

        print(f'Жанр на удаление {genre_to_delete.id=} {genre_to_delete.name=}')

        session.delete(genre_to_delete)

        print('Жанр удален из базы данных')
        session.commit()

    except Exception as e:
        # Если что-то не так, то откатываемся
        session.rollback()
        raise e

    finally:
        # Закрыть сессию
        session.close()




if __name__ == '__main__':
    main()