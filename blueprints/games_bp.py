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
    stmt = db.select(Game).order_by(Game.id) # Builds the query to retrieve all games
    games = db.session.scalars(stmt).all() # Executes the query with scalars and all to get all games
    return GameSchema(many=True).dump(games) # Returns all games with many=True as there will be more than one game 

# Retrieve one game 
@games_bp.route('/<int:game_id>', methods=['GET'])
def one_game(game_id):
    stmt = db.select(Game).filter_by(id=game_id) # Builds a query to get a game with an id that matches the id that has been passed in
    game = db.session.scalar(stmt) # Executes the query with scalar singular as there will only be one game
    if game: # If game is truthy (it exists) then return the game
        return GameSchema().dump(game)
    else:
        return {'error':'Game not found'}, 404 # If game is not truthy (it does not exist) then return a corresponding error message 

# Adds a new game for reviewing - only admins can do this
@games_bp.route('/', methods=['POST'])
@jwt_required() # Gets the JSON web token from the user as users must be logged in to add a game to the database
def add_game():
    admin_required() # Checks if the user is an admin as only admins can add games
    try:
        game_info = GameSchema().load(request.json) # Deserialise the JSON data in the request and convert it into a python object based on the Game Schema
        game = Game(
            title=game_info['title'],
            genre=game_info['genre'],
            description=game_info['description'],
            platforms=game_info['platforms']
        ) # Pass the information in the request into a new instance of the Game Schema
        db.session.add(game) # Add and commit the game
        db.session.commit()
        return GameSchema().dump(game), 201 # Return the freshly created game
    except IntegrityError:
        return {'error': 'Game already exists'}, 409 # If the game already exists return a corresponding error message
    except KeyError:
        return {'error':'please provide all details of the game'}, 400 # If the request is missing key details return a corresponding error message
    
# Updates a game - A game may be added to new platforms some time after release
@games_bp.route('/<int:game_id>', methods=['PUT', 'PATCH'])
@jwt_required() # Gets the JSON web token from the user 
def update_game(game_id):
    game = Game.query.get(game_id) # queries Games for a game with an id that matches the id that was passed in
    if game: # if game is truthy (it exists and id matches the id that was passed in) then continue the request
        admin_required() # Checks if the user is an admin as only admins are allowed to edit game details 
        game_info = GameSchema().load(request.json, partial=True) # Deserialise the JSON data in the request and convert into a python object based on the Game Schema with partial=True as not all fields will be required if only one field needs updating
        game.title = game_info.get('title', game.title),
        game.genre = game_info.get('genre', game.genre),
        game.description = game_info.get('description', game.description),
        game.platforms = game_info.get('platforms', game.platforms)
        db.session.commit() # Commit the changes 
        return GameSchema().dump(game) # Return the freshly updated game
    else: 
        return {'error': 'game not found'}, 404 # If no such game
    
# Delete a game - unlikely in a real world scenario but still essential functionality to have
@games_bp.route('/<int:game_id>', methods=['DELETE'])
@jwt_required()
def delete_game(game_id):
    stmt = db.select(Game).filter_by(id=game_id) # Prepare the statement to select a game with an id that matchs the id that was passed in
    game = db.session.scalar(stmt) # Execute the statement with scalar singular as only game will be retrieved
    if game: # If game is truthy (it exists) then continue the request
        admin_required()
        db.session.delete(game) # Delete the game 
        db.session.commit() # Commit the changes 
        return {'message': 'game deleted'}, 200 # Return a confirmation message
    else: 
        return {'error': 'game not found'}, 404 # If game is not truthy then return a corresponding error message 