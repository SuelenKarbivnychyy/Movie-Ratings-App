"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db
from datetime import datetime

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title = title, overview = overview, release_date = release_date, poster_path = poster_path)

    return movie

def show_movies():
    """Shows all movies."""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """Get a movie by its id."""

    return Movie.query.get(movie_id)

def show_users():
    """Shows all users."""

    return User.query.all()

def get_user_by_id(user_id):
    """Get a user by their id."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    return rating

def get_rating_by_user(user_id, movie_id):
    """Return rating by user."""

    return Rating.query.filter(Rating.user_id == user_id,
                 Rating.movie_id == movie_id).first()

    

if __name__ == '__main__':
    from server import app
    connect_to_db(app)