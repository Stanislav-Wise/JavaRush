from db.session import SessionLocal
from models.genry import Genre
from models.movie import Movie
from models.review import Review


def main():
    session = SessionLocal()

    try:

        print('Update genre')

        # WHERE = 'Action'
        genre_to_update = session.query(Genre).filter_by(name='Mult').first()

        if genre_to_update is None:
            print('Жанр Action не найден.')

        genre_to_update.name = 'Multfilm'
        session.commit()

        print('Жанр Action обновлен')

        new_genre = session.query(Genre).filter_by(id=genre_to_update.id).first()

        print(f'{genre_to_update.id=} {genre_to_update.name=}')
    except Exception as e:
        # Если что-то не так, то откатываемся
        session.rollback()
        raise e

    finally:
        # Закрыть сессию
        session.close()




if __name__ == '__main__':
    main()