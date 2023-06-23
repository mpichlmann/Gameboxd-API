from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

# GAMES MODEL
class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    genre = db.Column(db.String(100))
    description = db.Column(db.Text())
    platforms = db.Column(db.String(100))

class GameSchema(ma.Schema):
    title = fields.String(required=True, validate=Length(min=1))
    genre = fields.String(required=True)
    description = fields.String(required=True)
    platforms = fields.String(required=True)

    class Meta:
        fields = ('id', 'title', 'genre', 'description', 'platforms')