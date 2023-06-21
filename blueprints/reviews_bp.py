from init import db
from flask import Blueprint, request
from models.review import Review, ReviewSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError

reviews_bp = Blueprint('reviews', __name__, url_prefix='/reviews')


@reviews_bp.route('/')
def all_reviews():
    stmt = db.select(Review).order_by(Review.id)
    games = db.session.scalars(stmt).all()
    return ReviewSchema(many=True).dump(games)

@reviews_bp.route('/add', methods=['POST'])
@jwt_required()
def add_review():
    try:
        review_info = ReviewSchema().load(request.json, partial=True)
        review = Review(
            title=review_info['title'],
            rating=review_info['rating'],
            body=review_info['body'],
            user_id=get_jwt_identity()
        )
        db.session.add(review)
        db.session.commit()
        return ReviewSchema().dump(review), 201
    except KeyError:
        return {'error':'Missing key details of review'}, 400
