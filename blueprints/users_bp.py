from init import db
from flask import Blueprint, request
from models.user import User, UserSchema
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required, admin_or_owner_required

users_bp = Blueprint('users', __name__, url_prefix='/users')

# Get all users 
@users_bp.route('/', methods=['GET'])
def all_users():
    stmt = db.select(User).order_by(User.id) # Prepares the query to retrieve all users 
    users = db.session.scalars(stmt).all() # Executes the query 
    return UserSchema(many=True, exclude=['password', 'reviews']).dump(users) # Returns all users excluding passwords, and their reviews for security and clarity

# Get a specific user 
@users_bp.route('/<int:user_id>', methods=['GET'])
def one_user(user_id):
    stmt = db.select(User).filter_by(id=user_id) # Prepares the query to get a user with an id that matches the id that was passed in
    user = db.session.scalar(stmt) # Executes the query
    if user: # If the user is truthy (if the user exists) then return the user
        return UserSchema(exclude=['password', 'reviews']).dump(user)
    else:
        return {'error':'User not found'}, 404 # If the user does not exist return a corresponding error message

# Update a user - change name, email, or password  
@users_bp.route('/<int:user_id>', methods=['PUT', 'PATCH'])
@jwt_required() # Get the JSON web token from the request
def update_user(user_id):
    user = User.query.get(user_id) # Query users for a user with an id that matches the id that was passed in
    if user: # If user is truthy (the user exists) continue the request
        admin_or_owner_required(user_id) # Check if the current user is an admin or has an id that matches the id that was passed in
        user_info = UserSchema().load(request.json, partial=True) # Deserialise the JSON data in the request and convert it into a python object based on the user schema with partial = True as not all fields may require updating
        user.name = user_info.get('name', user.name)
        user.email = user_info.get('email', user.email)
        user.password = user_info.get('password', user.password)
        db.session.commit() # commit the changes 
        return UserSchema(exclude=['password', 'reviews']).dump(user) # return the freshly updated user excluding password and their reviews
    else:
        return {'error': 'User not found'}, 404 # If the user is not truthy (they do not exist) return a corresponding error message

# Update a user - make admin - only admins can do this 
@users_bp.route('/make_admin/<int:user_id>', methods=['PUT', 'PATCH'])
@jwt_required() # Get the JSON web token from the request
def make_admin(user_id):
    user = User.query.get(user_id) # Query users for a user with an id that matches the id that was passed in
    if user: # If the user is truthy (they exist) then continue the request
        admin_required() # Check if the current user is an admin as only admins can create other admins
        user.is_admin = True # Set is_admin for the user that has been passed in to true
        db.session.commit() # commit the changes 
        return {'message': f'user with ID {user.id} is now an admin'}, 200 # Return a confirmaton message
    else:
        return {'error': 'User not found'}, 404 # If user is not truthy (they do not exist) return a corresponding error message

# Delete a user - only admins can do this 
@users_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required() # Get the JSON web token from the request
def delete_user(user_id):
    user = User.query.get(user_id) # Query users for a user with an id that matches the id that was passed in
    if user: # If user is truthy (they exist) continue the request
        admin_required() # Check if the current user is an admin as only admins can delete users
        db.session.delete(user) # Delete the user 
        db.session.commit() # Commit the changes
        return {'message': 'User deleted successfully'}, 200 # Return a confirmation message
    else:
        return {'error': 'User not found'}, 404 # If the user is not truthy (they do not exist) return a corresponding error message




