from init import db, bcrypt
from flask import Blueprint, request
from models.game import Game, GameSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError
from blueprints.auth_bp import admin_required

games_bp = Blueprint('games', __name__, url_prefix='/games')


@games_bp.route('/')
@jwt_required()
def all_games():
    stmt = db.select(Game).order_by(Game.id)
    games = db.session.scalars(stmt).all()
    return GameSchema(many=True).dump(games)


@games_bp.route('/add', methods=['POST'])
@jwt_required()
def add_game():
    admin_required()
    try:
        game_info = GameSchema().load(request.json)
        game = Game(
            title=game_info['title'],
            genre=game_info['genre'],
            description=game_info['description'],
            platforms=game_info['platforms']
        )
        db.session.add(game)
        db.session.commit()
        return GameSchema().dump(game), 201
    except IntegrityError:
        return {'error': 'Game already exists'}, 409
    except KeyError:
        return {'error':'Missing key details of game'}, 400