from db.session import SessionLocal
from models.genry import Genre
from models.movie import Movie
from models.review import Review


session = SessionLocal()

# CRUD

# Create
# Создать новый объект в памяти python
new_genre = Genre(name="Comedy")
# Добавили объект в сессию
session.add(new_genre)
# Фиксируем изменения
session.commit()

# Read
genres = session.query(Genre).all()
genres = session.query(Genre).first()
genres = session.query(Genre).filter_by(name='Comedy')
genres = session.query(Genre).filter_by(name='Comedy').first()


# Update
# 1. Найти объект, например
my_genre = session.query(Genre).filter_by(name='Comedy').first()
# 2. Меняем поле
my_genre.name = 'Комедия'
# 3. Фиксируем изменения
session.commit()


# Delete
# 1. Найти объект, например
my_genre = session.query(Genre).filter_by(name='Comedy').first()
# 2. Удаляем объект
session.delete(my_genre)
# 3. Фиксируем изменения
session.commit()



# Если что-то не так, то откатываемся
session.rollback()
