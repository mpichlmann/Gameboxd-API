from init import db
from flask import Blueprint
from models.user import User, UserSchema

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/')
def all_users():
    stmt = db.select(User).order_by(User.id)
    games = db.session.scalars(stmt).all()
    return UserSchema(many=True).dump(games)