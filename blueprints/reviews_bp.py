from init import db
from flask import Blueprint
from models.review import Review, ReviewSchema

reviews_bp = Blueprint('reviews', __name__, url_prefix='/reviews')


@reviews_bp.route('/')
def all_reviews():
    stmt = db.select(Review).order_by(Review.id)
    games = db.session.scalars(stmt).all()
    return ReviewSchema(many=True).dump(games)