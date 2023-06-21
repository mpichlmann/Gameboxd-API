# Web Server API 
from flask import Flask
from os import environ
from blueprints.cli_bp import cli_bp
from blueprints.auth_bp import auth_bp
from blueprints.games_bp import games_bp
from blueprints.reviews_bp import reviews_bp
from blueprints.users_bp import users_bp
from blueprints.comments_bp import comments_bp
from init import db, ma, bcrypt, jwt

# Configuration and Instances 
def setup():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(cli_bp)
    app.register_blueprint(auth_bp)

    app.register_blueprint(games_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(comments_bp)
    app.register_blueprint(users_bp)

    @app.route('/')
    def hello():
        return 'HELLO WORLD'

    return app


