from init import db, ma 
from marshmallow import fields
from marshmallow.validate import Range

# REVIEW MODEL 
class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    body = db.Column(db.Text(), nullable=False)
    date_created = db.Column(db.Date())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id', ondelete='CASCADE'), nullable=False)

    user = db.relationship('User', back_populates='reviews')
    comments = db.relationship('Comment', back_populates='review', cascade='all, delete')

class ReviewSchema(ma.Schema):
    title = fields.String(required=True)
    rating = fields.Integer(required=True, validate=Range(min=0, max=5))
    body = fields.String(required=True)
    game_id = fields.Integer(required=True)

    user = fields.Nested('UserSchema', exclude=['reviews', 'password'])
    comments = fields.Nested('CommentSchema', only=['body', 'user_id'], many=True) 

    class Meta:
        fields = ('id', 'title', 'rating', 'body', 'date_created', 'user', 'game_id', 'comments')