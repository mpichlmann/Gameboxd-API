# Web Server API 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
from dotenv import load_dotenv
from datetime import date
from flask_marshmallow import Marshmallow
from blueprints.cli_bp import cli_bp
from blueprints.games_bp import games_bp
from init import db, ma


load_dotenv()

# Configuration and Instances 
def setup():
    app = Flask(__name__)

    app.config['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(cli_bp)
    app.register_blueprint(games_bp)

    @app.route('/')
    def hello():
        return 'HELLO WORLD'

    return app


