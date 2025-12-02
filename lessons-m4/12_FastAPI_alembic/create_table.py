from db.session import engine, Base
from models.genry import Genre
from models.movie import Movie
from models.review import Review


if __name__ == '__main__':
    print('Creating tables...')
    # Base.metadata.create_all(bind=engine)
    print('Tables created.')