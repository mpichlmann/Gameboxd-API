from init import db, ma 

# COMMENT MODEL 
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text())
    date_created = db.Column(db.Date())

class CommentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'body', 'date_created')