from init import db, ma 

# REVIEW MODEL 
class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    body = db.Column(db.Text())
    date_created = db.Column(db.Date())

class ReviewSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'rating', 'body', 'date_created')