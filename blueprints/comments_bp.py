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

# Retrieve all comments for all games 
@comments_bp.route('/')
def all_comments():
    stmt = db.select(Comment).order_by(Comment.id)
    games = db.session.scalars(stmt).all()
    return CommentSchema(many=True).dump(games)

# Retrieve all comments by a specifc user
@comments_bp.route('/user/<int:user_id>')
def get_comments_by_user(user_id):
    user = User.query.get(user_id)
    if user:
        comments = Comment.query.filter_by(user_id=user_id).all()
        if comments:
            comment_schema = CommentSchema(many=True)
            return comment_schema.dump(comments)
        else: return {'error': 'No comments from that user were found.'}, 404
    else:
        return {'error': 'User not found.'}, 404



# Retrieve all comments for a specific review 
@comments_bp.route('/review/<int:review_id>')
def get_comments_by_review(review_id):
    review = Review.query.get(review_id)
    if review:
        comments = Comment.query.filter_by(review_id=review_id).all()
        if comments:
            comment_schema = CommentSchema(many=True)
            return comment_schema.dump(comments)
        else:
            return {'error': 'No comments for the specified review ID'}, 404
    else:
        return {'error': 'Review not found'}, 404


# Create a new comment 
@comments_bp.route('/', methods=['POST'])
@jwt_required()
def add_comment():
    try:
        comment_info = CommentSchema().load(request.json)
        comment = Comment(
            body=comment_info['body'],
            date_created=date.today(),
            user_id = get_jwt_identity(),
            review_id = comment_info['review_id']
        )
        db.session.add(comment)
        db.session.commit()
        return CommentSchema().dump(comment), 201
    except IntegrityError:
        return {'error': 'No such review exists to be commented on - check review_id is correct'}, 409
    except KeyError:
        return {'error':'please provide all details of the review'}, 400
    
# Update a comment - only the owner or admin can do this
@comments_bp.route('/<int:comment_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_comment(comment_id):
    stmt = db.select(Comment).filter_by(id=comment_id)
    comment = db.session.scalar(stmt)
    comment_info = CommentSchema().load(request.json)
    if comment:
        admin_or_owner_required(comment.user_id)
        comment.body = comment_info.get('body', comment.body),
        db.session.commit()
        return ReviewSchema().dump(comment)
    else: 
        return {'error': 'Comment not found'}, 404 

# Delete a comment - only the owner or admin can do this 
@comments_bp.route('/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete_comment(comment_id):
    stmt = db.select(Comment).filter_by(id=comment_id)
    comment = db.session.scalar(stmt)
    if comment:
        admin_or_owner_required(comment.user_id)
        db.session.delete(comment)
        db.session.commit()
        return {'message': 'Comment deleted'}, 200
    else:
        return {'error': 'Comment not found'}, 404