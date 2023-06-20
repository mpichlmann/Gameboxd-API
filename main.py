# Web Server API 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
from dotenv import load_dotenv
from datetime import date
load_dotenv()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
db = SQLAlchemy(app)

# USER MODEL 
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

# REVIEW MODEL 
class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text())
    body = db.Column(db.Text())
    date_created = db.Column(db.Date())

# COMMENT MODEL 
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text())
    date_created = db.Column(db.Date())

# GAMES MODEL
class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String)
    description = db.Column(db.Text())
    platform = db.Column(db.String)

@app.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print("created tables")

@app.cli.command('seed')
def seed_db():
    games = [
    Game(
        title = 'Resident Evil 4 Remake',
        genre = 'Action/Horror',
        description = 'Survive monsters and horrors, and stop an evil plot',
        platform = 'Playstation, Xbox, PC'
    ),
    Game(
        title = 'Elden Ring',
        genre = 'RPG',
        description = 'Explore an open world, become Elden Lord and unite the Elden Ring!',
        platform = 'Playstation, Xbox, PC'
    ),
    ]
    
    db.session.query(Game).delete()
    db.session.add_all(games)
    db.session.commit()


    print('tables seeded') 


@app.route('/hello')
def hello():
    return 'lol'

