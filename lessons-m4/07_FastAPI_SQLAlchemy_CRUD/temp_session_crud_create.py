from db.session import SessionLocal
from models.genry import Genre
from models.movie import Movie
from models.review import Review


def main():
    session = SessionLocal()

    try:
        # Создать новые объекты в памяти python
        genre_1 = Genre(name="Комедия")
        genre_2 = Genre(name="Боевик")
        genre_3 = Genre(name="Фантасика")

        # # Добавили объект в сессию (1 вариант)
        # session.add(genre_1)
        # session.add(genre_2)
        # session.add(genre_3)

        # Добавили объект в сессию (2 вариант)
        session.add_all([genre_1, genre_2, genre_3])

        # Фиксируем изменения
        session.commit()

        # Read
        genres = session.query(Genre).all()

        print('Все жанры в базе')


        for genre in genres:
            print(f'{genre.id=} {genre.name=}')

    except Exception as e:
        # Если что-то не так, то откатываемся
        session.rollback()
        raise e

    finally:
        # Закрыть сессию
        session.close()


if __name__ == '__main__':
    main()