from init import db, ma 

# GAMES MODEL
class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    genre = db.Column(db.String(100))
    description = db.Column(db.Text())
    platforms = db.Column(db.String(100))

class GameSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'genre', 'description', 'platforms')