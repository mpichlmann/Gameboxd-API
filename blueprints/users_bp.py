from init import db
from flask import Blueprint, request
from models.user import User, UserSchema
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/')
def all_users():
    stmt = db.select(User).order_by(User.id)
    games = db.session.scalars(stmt).all()
    return UserSchema(many=True).dump(games)


# Update a user - change name, email, or password 


# Update a user - make admin - only admins can do this 
@users_bp.route('/<int:user_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def make_admin(user_id):
    user = User.query.get(user_id)
    if user:
        admin_required()
        user.is_admin = True
        db.session.commit()
        return {'message': f'user with ID {user.id} is now an admin'}
    else:
        return {'error': 'User not found'}, 404

# Delete a user 




