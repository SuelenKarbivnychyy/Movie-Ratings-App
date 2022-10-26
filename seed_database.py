"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
from model import User, Rating, Movie
import server
import model

os.system("dropdb ratings")
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    title = movie['title']
    overview = movie['overview']
    release_date = datetime.strptime(movie['release_date'], "%Y-%m-%d")
    poster_path = movie['poster_path']
    

    new_movie = Movie.create(title, overview, release_date, poster_path)
    movies_in_db.append(new_movie)

model.db.session.add_all(movies_in_db)
model.db.session.commit()

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'
    new_user = User.create(email, password)
    model.db.session.add(new_user)

    for _ in range(10):
        new_rating = Rating.create(new_user, choice(movies_in_db), randint(1,5))
        model.db.session.add(new_rating)

model.db.session.commit()
