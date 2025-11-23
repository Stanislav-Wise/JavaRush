from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    rating = Column(Integer, nullable=False)
    text = Column(Text)

    movies = relationship("Movie", back_populates="reviews") # review.movie.title