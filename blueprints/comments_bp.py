from init import db
from flask import Blueprint, request
from models.comment import Comment, CommentSchema
from models.review import Review, ReviewSchema
from models.user import User, UserSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import date
from sqlalchemy.exc import IntegrityError
from blueprints.auth_bp import admin_or_owner_required

comments_bp = Blueprint('comments', __name__, url_prefix='/comments')

# Retrieve all comments for all reviews 
@comments_bp.route('/', methods=['GET'])
def all_comments(): 
    stmt = db.select(Comment).order_by(Comment.id) # builds a query to get all comments
    comments = db.session.scalars(stmt).all() # executes the query using scalars and .all() as there will be more than one comment
    return CommentSchema(many=True).dump(comments) # returns the comment schema for all comments with many = True

# Retrieve all comments by a specifc user
@comments_bp.route('/user/<int:user_id>', methods=['GET'])
def get_comments_by_user(user_id):
    user = User.query.get(user_id) # queries the Users for a matching id to the id that has been passed into the function from the route
    if user: # If user is truthy (if a user with an id that matches exists)
        comments = Comment.query.filter_by(user_id=user_id).all() # Quries comment model for comments with a corresponding user id
        if comments: # If comments is truthy (if comments with a corresponding user id exists)
            comment_schema = CommentSchema(many=True) # Initialise a comment schema to serialise multiple comments
            return comment_schema.dump(comments) # Serialise comments and return the result 
        else: return {'error': 'No comments from that user were found.'}, 404 # If comments is not truthy (no comments with that user id exist) return a corresponding error
    else:
        return {'error': 'User not found.'}, 404 # if user is not truthy (no user with that id exists) return a corresponding error

# Retrieve all comments for a specific review 
@comments_bp.route('/review/<int:review_id>', methods=['GET'])
def get_comments_by_review(review_id):
    review = Review.query.get(review_id) # Queries the Reviews based on the ID that has been passed in
    if review: # If the review is truthy (it exists) retrieve all comments associated with it
        comments = Comment.query.filter_by(review_id=review_id).all()
        if comments: # If comments are truthy (they exist) initialise a CommentSchema with many=True to serialise them 
            comment_schema = CommentSchema(many=True)
            return comment_schema.dump(comments) # Serialise and return all comments for the corresponding Review ID
        else:
            return {'error': 'No comments for the specified review ID'}, 404 # If no comments are found, return a corresponding error message
    else:
        return {'error': 'Review not found'}, 404 # If no review is found that matches the provided ID return a corresponding error message

# Create a new comment 
@comments_bp.route('/', methods=['POST'])
@jwt_required() # Get the JSON web token from the request - as users must be logged in before commenting
def add_comment():
    try:
        comment_info = CommentSchema().load(request.json) # Deserialise the JSON data in the request
        comment = Comment( # Pass the information in the request into a new instance of the Comment Schema
            body=comment_info['body'],
            date_created=date.today(),
            user_id = get_jwt_identity(),
            review_id = comment_info['review_id']
        )
        db.session.add(comment) # Add and commit the comment
        db.session.commit() 
        return CommentSchema().dump(comment), 201 # Return the freshly created comment
    except IntegrityError:
        return {'error': 'No such review exists to be commented on - check review_id is correct'}, 409 # If no review exists to be commented on return a corresponding error message
    except KeyError:
        return {'error':'Please provide all details of the review'}, 400 # If the comment is missing critical details provide a corresponding error message
    
# Update a comment - only the owner or admin can do this
@comments_bp.route('/<int:comment_id>', methods=['PUT', 'PATCH'])
@jwt_required() # Get the JSON web token from the request - as users must be logged in before updating a comment
def update_comment(comment_id):
    comment = Comment.query.get(comment_id) # Query comments for a comment that has a matching id to the comment_id that has been passed in
    if comment: # if the comment is truthy (it exists and has a matching id) then continue the request
        admin_or_owner_required(comment.user_id) # 
        comment_info = CommentSchema().load(request.json, partial=True) # Deserialise the JSON data in the request
        comment.body = comment_info.get('body', comment.body) # Pass the new body data into the comment
        db.session.commit() # Commit the changes 
        return ReviewSchema().dump(comment) # Return the freshly updated comment
    else: 
        return {'error': 'Comment not found'}, 404 

# Delete a comment - only the owner or admin can do this 
@comments_bp.route('/<int:comment_id>', methods=['DELETE'])
@jwt_required() # Get the JSON web token from the request
def delete_comment(comment_id):
    stmt = db.select(Comment).filter_by(id=comment_id) # Prepare the query to select a comment with an id matching the id that has been passed in
    comment = db.session.scalar(stmt) # Execute the query
    if comment: # If the comment is truthy (it exists and matches the id that has been passed in) continue the request
        admin_or_owner_required(comment.user_id) # Check if the user is an admin or has a user id that matches the user id that is attached to the retrieved comment
        db.session.delete(comment) # Delete the comment from the database
        db.session.commit() # Commit the changes
        return {'message': 'Comment deleted'}, 200 # Return a confirmation message
    else:
        return {'error': 'Comment not found'}, 404 # If the comment is not truthy then return an error with a corresponding message