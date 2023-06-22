from init import db, ma
from marshmallow import fields 

# COMMENT MODEL 
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text(), nullable=False)
    date_created = db.Column(db.Date())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'), nullable=False)

    review = db.relationship('Review', back_populates='comments')

class CommentSchema(ma.Schema):
    review = fields.Nested('ReviewSchema', only=['title'])

    class Meta:
        fields = ('id', 'body', 'date_created', 'user_id', 'review_id', 'review')