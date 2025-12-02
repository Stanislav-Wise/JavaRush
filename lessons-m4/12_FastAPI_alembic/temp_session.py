from db.session import SessionLocal
from models.genry import Genre
from models.movie import Movie
from models.review import Review


# Открыть сессию
session = SessionLocal()

# Создать новый объект в памяти python
new_genre = Genre(name="Comedy")

# Добавили объект в сессию
session.add(new_genre)

# Фиксируем изменения
session.commit()

# Обновить объект из базы
session.refresh(new_genre)


genres = session.query(Genre).all()

for genre in genres:
    print(f'{genre.id=} {genre.name=}')

# Закрыть сессию
session.close()