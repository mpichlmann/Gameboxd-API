# Web Server API 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
from dotenv import load_dotenv
from datetime import date
from flask_marshmallow import Marshmallow
load_dotenv()

# Configuration and Instances 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
db = SQLAlchemy(app)
ma = Marshmallow(app)

# USER MODEL 
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')

# REVIEW MODEL 
class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    body = db.Column(db.Text())
    date_created = db.Column(db.Date())

class ReviewSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'rating', 'body', 'date_created')

# COMMENT MODEL 
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text())
    date_created = db.Column(db.Date())

class CommentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'body', 'date_created')

# GAMES MODEL
class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100))
    description = db.Column(db.Text())
    platforms = db.Column(db.String(100))

class GameSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'genre', 'description', 'platforms')
        ordered = True

# Create Tables 
@app.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print("created tables")

# Seed Tables
@app.cli.command('seed')
def seed_db():
    #Seed Users
    users = [
        User(
            name = 'Adam Minister',
            email = 'admin@gameboxd.com',
            password = 'password123',
            is_admin = True
        ),
        User(
            name = 'John Doe',
            email = 'johndoe@test.com',
            password = 'testpass123',
            is_admin = False
        ),
    ]
    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()

    #Seed Reviews
    reviews = [
        Review(
            title = 'FromSoftwares latest masterpiece',
            rating = 5,
            body = 'the game is awesome, I loved it! Incredible world design and combat encounters',
            date_created = date.today(),
        ),
        Review(
            title = 'RE4 leaves a lot to be desired',
            rating = 3,
            body = 'Its okay, not amazing, not awful. The gameplay is a little dated',
            date_created = date.today(),
        ),
    ]
    db.session.query(Review).delete()
    db.session.add_all(reviews)
    db.session.commit()

    #Seed Comments
    comments = [
        Comment(
        body = 'I agree, elden ring is a fantastic game',
        date_created = date.today(),
        ),
        Comment(
        body = 'I disagree, I think RE4 is a fantastic modern remake',
        date_created = date.today(),
        )
    ]
    db.session.query(Comment).delete()
    db.session.add_all(comments)
    db.session.commit()

    #Seed Games
    games = [
        Game(
            title = 'Resident Evil 4 Remake',
            genre = 'Horror',
            description = 'Survive monsters and horrors, and stop an evil plot',
            platforms = 'Playstation, Xbox, PC'
        ),
        Game(
            title = 'Elden Ring',
            genre = 'RPG',
            description = 'Explore an open world, become Elden Lord and unite the Elden Ring!',
            platforms = 'Playstation, Xbox, PC'
        ),
    ]
    db.session.query(Game).delete()
    db.session.add_all(games)
    db.session.commit()
    
    print('tables seeded') 


@app.route('/games')
def all_games():
    stmt = db.select(Game).order_by(Game.id)
    games = db.session.scalars(stmt).all()
    return GameSchema(many=True).dump(games)

@app.route('/users')
def all_users():
    stmt = db.select(User).order_by(User.id)
    games


@app.route('/')
def hello():
    return 'HELLO WORLD'


