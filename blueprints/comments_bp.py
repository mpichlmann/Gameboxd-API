from init import db
from flask import Blueprint
from models.comment import Comment, CommentSchema

comments_bp = Blueprint('comments', __name__, url_prefix='/comments')


@comments_bp.route('/')
def all_comments():
    stmt = db.select(Comment).order_by(Comment.id)
    games = db.session.scalars(stmt).all()
    return CommentSchema(many=True).dump(games)