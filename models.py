from sqlalchemy import Column, Integer, String, Float, BigInteger, ForeignKey
from db import Base

class Movie(Base):
    __tablename__ = 'movies'
    movie_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    genres = Column(String(255), nullable=False)

class Rating(Base):
    __tablename__ = 'ratings'
    user_id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.movie_id'), primary_key=True)
    rating = Column(Float, nullable=False)
    timestamp = Column(BigInteger, nullable=True)

