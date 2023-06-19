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
    __tablename__='reviews'

    id = db.Column(db.Integer, primary_key=True)

    rating = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text())
    body = db.Column(db.Text())
    date_created = db.Column(db.Date())

db.create_all()



@app.route('/hello')
def hello():
    return 'lol'


if __name__ == '__main__':
    app.run(debug=True)

