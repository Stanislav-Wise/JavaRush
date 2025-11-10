from db.session import SessionLocal
from models.genry import Genre
from models.movie import Movie
from models.review import Review

# from models.movie import Movie
# from models.review import Review


# session = SessionLocal()
#
# new_genre = Genre(name="Action")
# session.add(new_genre)
#
# new_genre = Genre(name="Mult")
# session.add(new_genre)
#
# new_genre = Genre(name="Melodrama")
# session.add(new_genre)
# session.commit()
# session.close()



session = SessionLocal()
genre = session.query(Genre).filter_by(name='Fantasy').first()

new_movie = Movie(
    title = 'Matrix 2',
    year = 2005,
    description = 'The Matrix 2',
    genre=genre
)
#
# new_movie = Movie(
#     title = 'Matrix',
#     year = 1999,
#     description = 'The Matrix',
#     genre_id=genre.id
# )

session.add(new_movie)
session.commit()
session.close()