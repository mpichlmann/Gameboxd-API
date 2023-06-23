from init import db
from flask import Blueprint, request
from models.game import Game, GameSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError
from blueprints.auth_bp import admin_required

games_bp = Blueprint('games', __name__, url_prefix='/games')

# Retrives all games 
@games_bp.route('/', methods=['GET'])
def all_games():
    stmt = db.select(Game).order_by(Game.id)
    games = db.session.scalars(stmt).all()
    return GameSchema(many=True).dump(games)

# Retrieve one game 
@games_bp.route('/<int:game_id>')
def one_game(game_id):
    stmt = db.select(Game).filter_by(id=game_id)
    game = db.session.scalar(stmt)
    if game: 
        return GameSchema().dump(game)
    else:
        return {'error':'Game not found'}, 404

# Adds a new game for reviewing - only admins can do this
@games_bp.route('/', methods=['POST'])
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
        return {'error':'please provide all details of the game'}, 400
    
# Updates a game - A game may be added to new platforms some time after release
@games_bp.route('/<int:game_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_game(game_id):
    game = Game.query.get(game_id)
    if game:
        admin_required()
        game_info = GameSchema().load(request.json, partial=True)
        game.title = game_info.get('title', game.title),
        game.genre = game_info.get('genre', game.genre),
        game.description = game_info.get('description', game.description),
        game.platforms = game_info.get('platforms', game.platforms)
        db.session.commit()
        return GameSchema().dump(game)
    else: 
        return {'error': 'review not found'}, 404
    
# Delete a game - unlikely in a real world scenario but still essential functionality to have
@games_bp.route('/<int:game_id>', methods=['DELETE'])
@jwt_required()
def delete_game(game_id):
    stmt = db.select(Game).filter_by(id=game_id)
    game = db.session.scalar(stmt)
    if game:
        admin_required()
        db.session.delete(game)
        db.session.commit()
        return {'message': 'game deleted'}, 200
    else: 
        return {'error': 'game not found'}, 404