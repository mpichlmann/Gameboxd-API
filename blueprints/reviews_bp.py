from init import db
from flask import Blueprint, request, jsonify
from models.review import Review, ReviewSchema
from models.game import Game, GameSchema
from models.user import User, UserSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from datetime import date
from blueprints.auth_bp import admin_or_owner_required

reviews_bp = Blueprint('reviews', __name__, url_prefix='/reviews')

# Get all reviews of all games - no login required
@reviews_bp.route('/', methods=['GET'])
def all_reviews():
    stmt = db.select(Review).order_by(Review.id) # Builds query to retrieve all reviews
    reviews = db.session.scalars(stmt).all() # Executes query with scalars and all to get all reviews
    return ReviewSchema(many=True).dump(reviews) # Returns all reviews with many=True as there will be more than one review

# Get a specific review - no login required
@reviews_bp.route('/<int:review_id>', methods=['GET'])
def one_review(review_id):
    stmt = db.select(Review).filter_by(id=review_id) # Builds a query to get a review with an id that matches the id that was passed in
    review = db.session.scalar(stmt) # Executes the statement with scalar singular as there will only be one review
    if review: # If the review is truthy (it exists) continue the request
        return ReviewSchema().dump(review) # Return the review
    else:
        return {'error':'Review not found'}, 404 # If review is not truthy (it does not exist) then return a corresponding error message

# #Get all reviews for a specific game - no login required
@reviews_bp.route('/game/<int:game_id>', methods=['GET'])
def get_reviews_by_game(game_id):
    game = Game.query.get(game_id) # Query Games for a game with a matching id to the id that was passed in
    if game: # If game is truthy (it exists and the id matches) then continue the request
        reviews = Review.query.filter_by(game_id=game_id).all() # Query reviews for reviews with a matching game_id to the id that was passed in
        if reviews: # If reviews is truthy (a review exists with a matching id) continue the request
            review_schema = ReviewSchema(many=True) 
            return review_schema.dump(reviews) # Return the reviews with many=True as there may be more than review for the specified game 
        else:
            return {'error': 'No reviews found for the specified game ID.'}, 404 # If reviews is not truthy (there are no reviews for the specified game) return a corresponding error message
    else:
        return {'error': 'Game not found.'}, 404 # If game is not truthy (no such game with the specified id exists) return a corresponding error message
    
# Get all reviews from a specific user - no login required
@reviews_bp.route('/user/<int:user_id>', methods=['GET'])
def get_reviews_by_user(user_id):
    user = User.query.get(user_id) # Query Users for a user with a matching id to the id that was passed in
    if user: # If user is truthy (it exists and the id matches) then continue the request
        reviews = Review.query.filter_by(user_id=user_id).all() # Query reviews for reviews with a matching user_id to the id that was passed in
        if reviews: # If reviews is truthy (a review exists with a matching id) continue the request
            review_schema = ReviewSchema(many=True)
            return review_schema.dump(reviews) # Return the reviews with many=True as there may be more than review for the specified user 
        else:
            return {'error': 'No reviews found for the specified user ID.'}, 404 # If reviews is not truthy (there are no reviews for the specified user) return a corresponding error message
    else:
        return {'error': 'User not found.'}, 404 # If user is not truthy (no such game with the specified id exists) return a corresponding error message

# Add a review - must be logged in to do this 
@reviews_bp.route('/', methods=['POST'])
@jwt_required() # Get the JSON web token from the user as users must be logged in to add a review
def add_review():
    try:
        review_info = ReviewSchema().load(request.json) # Deserialise the JSON data in the request and convert it into a python object based on the review schema 
        review = Review(
            title=review_info['title'],
            rating=review_info['rating'],
            body=review_info['body'],
            date_created=date.today(),
            user_id = get_jwt_identity(),
            game_id = review_info['game_id']
        ) # Pass the corresponding info in the request into the fields in the schema
        db.session.add(review) # Add and commit the new review
        db.session.commit()
        return ReviewSchema().dump(review), 201 # Return the freshly created review
    except IntegrityError:
        return {'error': 'Game not found'}, 409 
    except KeyError:
        return {'error':'please provide all details of the review'}, 400 # If key details of the review are missing from the request return a corresponding error message
    
# Update a review - only the review owner or an admin can do this 
@reviews_bp.route('/<int:review_id>', methods=['PUT', 'PATCH'])
@jwt_required() # Get the JSON web token from the user as users must be logged in to edit a review
def update_review(review_id):
    review = Review.query.get(review_id) # Query reviews for a review with an id that matches the id that was passed in
    if review: # If the review is truthy (it exists) then continue the request
        admin_or_owner_required(review.user_id) # Check if the user id is an admin or the owner of the review
        review_info = ReviewSchema().load(request.json, partial=True) # Deserialise the JSON data in the request and convert it into a python object based on the review schema with partial = True as not all fields may require updating 
        review.title = review_info.get('title', review.title)
        review.rating = review_info.get('rating', review.rating)
        review.body = review_info.get('body', review.body)
        db.session.commit() # Commit the changes 
        return ReviewSchema(exclude=['user','comments']).dump(review) # Return the freshly updated review
    else: 
        return {'error': 'Review not found'}, 404 # If review is not truthy (it does not exist) return a corresponding error message
    
# Delete a review - only the review owner or an admin can do this 
@reviews_bp.route('/<int:review_id>', methods=['DELETE'])
@jwt_required() # Get the JSON web token from the user as users must be logged in to delete a review
def delete_review(review_id):
    stmt = db.select(Review).filter_by(id=review_id) # Prepare the query to select a review with an id matching the id that was passed in
    review = db.session.scalar(stmt) # Execute the query
    if review: # If the review is truthy (it exists) continue the request 
        admin_or_owner_required(review.user_id) # Check if the user is an admin or the owner of the review
        db.session.delete(review) # Delete the review
        db.session.commit() # Commit the changes
        return {'message':'Review deleted'}, 200 # Return a confirmation message
    else: 
        return {'error': 'Review not found'}, 404 # If the review is not truthy (it does not exist) return a corresponding error message