## R4 Identify key functionalities and benefits of an ORM, provide a nuanced discussion of each 
An ORM is an object relational mapper, such as SQL Alchemy, that allows developers to forgo using repetitive SQL queries and instead use much simpler and much more efficient standard programming language, such as python. ORMs work together with OOP (object oriented programming) to create higher level representations of databases within objects that can be more easily manipulated. Rather than having to manually input all the necessary SQL commands to create a table, insert data, and then manipulate that data, an ORM such as SQL alchemy allows for a class to be created in python, and for all the aforementioned actions to instead be performed on the class. 

Part of how ORMs work is by using what’s called a session. A session acts like a holding zone for all the queries that have been executed through code. By using a session it allows multiple queries to be stacked on top of each other and executed all at once, or only for certain queries to be executed under certain conditions. Once queries and other commands (such as deleting a table), have been added to the session, the session needs to be committed for the changes to take effect. This compartmentalisation of the database querying process is beneficial as it allows for a greater degree of debugging. Sessions can be tracked and more closely investigated to see what changes were made and when. Sessions can even be rolled back in the case that an unintended change was made to the database. 

Some of the benefits of using an ORM are that it speeds up development time and reduces development costs by providing a much more powerful and much more efficient method of data manipulation. ORMs also provide a much simpler method of handling relationships and associations between the database entities. The mapper provides ways of defining foreign/primary keys and ways of accessing objects through related entities, allowing for very complex queries that involve dependent data to be executed much more elegantly than through straight SQL. ORMs are also intended to create a degree of portability by allowing developers to simply configure the ORM drivers/adapters to work with the database system of choice without the need to adjust any of the main program code. Another benefit of ORMs is that they provide methods for data validation and data sanitisation, by constraining data in this way it helps to add a layer of integrity to the database and prevent unwanted instances of incorrect or incomplete data being referred to. Finally ORMs promote cleaner code practice that as a result allows a greater degree of collaboration and parallel development. 

## R8 Describe your projects models in terms of the relationships they have with each other
The models in the current project are as follows: 

Firstly there is the the user model: 
```python
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    reviews = db.relationship('Review', back_populates='user', cascade='all, delete')
```
This model contains the necessary user information and as users are responsible for creating reviews this model is related to the review model. To prevent instances of a review existing without a user, cascade deletes are used in order to delete all of the reviews associated with a user in the event that a user account is deleted. Observing the review model below reveals that just as the user model is related to the review model, the review model is also related to the user model. In the review model located below the user model is used to create a 'user_id' field that serves as a foreign key relating back to the id field in the user model. This is done so that all reviews from a specific user can be retrieved and so that reviews cannot be created without an associated user. Unlike in the user model, there is no cascading deletes set up in the db relationship on the review end of the two models, so that if a review is deleted the corresponding user account does not also get deleted, as this would not be the intended behaviour. The comment model is also related to the review model, with comments being nested within each instance of a review. With this relationship there *is* a cascading deletion set up, so that when a review is deleted the corresponding comments belonging to that review are also deleted, preventing orphaned comments from persisting in the database. 
```python
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
```
The review model is also related to the game model found below. As reviews cannot be created without a game that the review is intended for, the game_id field in the review model serves as a foreign key relating to the id field in the games model. This allows for the retrieval of all reviews for a specific game. As there is no need for games to be related to specific comments users or reviews there is no need to set up any relationships within the games model itself. Games instead are intended to be a distinct entity that other entities can access and create content around. 
```python
class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    genre = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    platforms = db.Column(db.String(100), nullable=False)
```
Finally there is the comment model, located below. This model is related to the review model, as reviews are inteded to be able to be commented on. This model connects to the users model and the reviews model utilishing each as a foreign key connecting to the respective id fields of each model. This is so that specific comments from users or specific comments for a review can be retrieved, and so that comments cannot be created without belonging to a user and a review. Just as is the case with reviews and users, in the comment model no cascading deletion is set up in the db relationship to reviews. This is done to prevent the deletion of a comment on a review from deleting the entire review that comment is associated with. 
```python
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text(), nullable=False)
    date_created = db.Column(db.Date())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id', ondelete='CASCADE'), nullable=False)

    review = db.relationship('Review', back_populates='comments')
```
The combination of these four models all working together allows users to create reviews for games, create comments on reviews, and delete each of these (as well as perform many other functions) all while maintaining database integrity. Through the appropriate use of relationships, foriegn keys, and cascading deletions there is no possibility of missing/orphaned data existing within the database. 

## R7 Third Party Services
Flask
SQLAlchemy
psycopg2
Marshmallow
Bcrypt
JSON Web Tokens 

## R10 Describe the way tasks are allocated and tracked in your project 



