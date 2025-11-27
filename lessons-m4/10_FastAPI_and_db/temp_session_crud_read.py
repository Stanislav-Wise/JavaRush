from db.session import SessionLocal
from models.genry import Genre
from models.movie import Movie
from models.review import Review


# session = SessionLocal()
#
# genre = session.query(Genre).first()
#
# print(genre.name)
#
# if genre:
#     for movie in genre.movies:
#         print(movie.title, movie.year)
#
# session.close()


session = SessionLocal()

movie = session.query(Movie).first()

print(movie.title)

print(movie.genre.name)

session.close()