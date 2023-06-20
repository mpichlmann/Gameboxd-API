from init import db
from flask import Blueprint
from models.game import Game, GameSchema

games_bp = Blueprint('games', __name__, url_prefix='/games')


@games_bp.route('/')
def all_games():
    stmt = db.select(Game).order_by(Game.id)
    games = db.session.scalars(stmt).all()
    return GameSchema(many=True).dump(games)