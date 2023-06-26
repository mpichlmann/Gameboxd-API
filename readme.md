## R0 - Installation and Set Up Instructions

Firstly make sure that the postgresql database server is running by opening your terminal and entering the following: 

Linux: 
```bash
sudo service postgresql start
```
Mac: 
```bash
brew service postgresql start
```
Once postgresql is running open it by entering the following: 
```bash
psql
```
Now create a new database called 'gameboxd' by entering the following: 
```bash
create database gameboxd;
```


```bash

```



```bash

```









## R1/R2 - Identifcation of problem being solved by this app and why it is a problem
Currently websites like letterboxd and yelp exist for reviewing movies and restaurants respectively. These websites offer a community unto themselves where users can share their thoughts and assessments, connect with each other, and build a following that respects and looks forward to their future contributions and recommendations. Currently no such equivalent for videogames exist. Videogame reviews certainly exist and videogame critics definitely exist, some very notable, however the problem is that no such platform equivalent to the aforementioned sites exist. 

With the way things are in their current state if people want to find reviews of videogames they have to visit large sites like IGN or Gamespot, or even go straight to the online store page of a specific videogame. The problem with these methods is that big mainstream organisations fail to deliver a diverse range of opinions, the constant browsing around for disparate reviews posted on different sites becomes tiresome, and the reviews themselves may only be referring to a specific version of the game (such as reviews on the PlayStation store page critiquing a games performance on the PlayStation rather than discussing the game itself).

If IGN reviews a game, then that single review is the only thing IGN has to say about the game, it’s not as if there is a second IGN review where people browsing their site can compare the two reviews and decide for themselves which one resonates more. People who do wish to compare and contrast differing opinions on a game will have to embark on the tedious task of browsing to multiple sites in search of a review that speaks to them. The problem becomes even larger when one considers the options available if they themselves would like to review a game and share their thoughts. Someone wanting to review a game would realistically have to choose between leaving a comment on a store page and posting a video to YouTube, where if they do not already have a strong following, both are likely to be lost in the sea of content. 

Plainly put, there exists no space that offers a community where people can be exposed to a range of opinions on games, connect with each other, contribute their thoughts, and build a following. The following proposed application will aim to rectify this problem. ‘Gameboxd’ is the working title for an API webserver that manages a relational database that will allow users to review games and connect with each other. Gameboxd solves the aforementioned problem by providing a centralised community specifically built for reviewing games, connecting with each other, and being exposed to a range of differing opinions and tastes. 


## R3 Why have you chosen this database system. What are the drawbacks compared to others?
The chosen database system for this project is PostgreSQL. PostgreSQL has many benefits and was well suited for the current project for a number of reasons. Postgres is an open source project with wide adoption and support, giving it a strong level of maintenance and makes finding solutions to any issues that may arise quick and easy. Postgres is supported on all major operating systems such as Windows, Mac and Linux, which means using it within the current project will allow a wider range of users to be able to enjoy the app. Scalability is another benefit of postgres with the database system being capable of handling up to thousands of terabytes of data, which for use in the proposed app would allow for significantly large amounts of users, games, reviews and comments without running into problems. Postgres also has wide compatibility and can be used with many different programming languages such as JavaScript, C, C++, Ruby, and Python in the current projects case (many other languages can also utilise postgres, these are just a few of the most popular). Reliability and integrity of data is another aspect of postgres that makes it a very good database system, postgres provides ACID (Atomicity, Consistency, Isolation, Durability) compliance guaranteeing transactions are processed with consistency, efficiency and reliability. 

While postgres has many benefits there are a few drawbacks in certain domains when compared to other database systems. Postgres has been reported to use more memory than other database systems, which means that in resource sparse settings it may not be the best choice. Postgres also does not support as many other open-source applications as other projects such as MySQL. Postgres has been considered to have a steeper learning curve than other database systems, both in the initial installation and set-up and in the everyday use, which can be an impediment to some users. There are limited NoSQL functionalities within postgres, which means it may not be as attractive of a choice of database when it comes to working with document-oriented or key-value workloads as some other database systems such as MongoDB. 

Despite these drawbacks postgres is still a very reliable and powerful relational database management system and is well suited for the current proposed project of an API Webserver designed to allow users to review games and comment on each other’s reviews.


## R4 Identify key functionalities and benefits of an ORM, provide a nuanced discussion of each 
An ORM is an object relational mapper, such as SQL Alchemy, that allows developers to forgo using repetitive SQL queries and instead use much simpler and much more efficient standard programming language, such as python. ORMs work together with OOP (object oriented programming) to create higher level representations of databases within objects that can be more easily manipulated. Rather than having to manually input all the necessary SQL commands to create a table, insert data, and then manipulate that data, an ORM such as SQL alchemy allows for a class to be created in python, and for all the aforementioned actions to instead be performed on the class. 

Part of how ORMs work is by using what’s called a session. A session acts like a holding zone for all the queries that have been executed through code. By using a session it allows multiple queries to be stacked on top of each other and executed all at once, or only for certain queries to be executed under certain conditions. Once queries and other commands (such as deleting a table), have been added to the session, the session needs to be committed for the changes to take effect. This compartmentalisation of the database querying process is beneficial as it allows for a greater degree of debugging. Sessions can be tracked and more closely investigated to see what changes were made and when. Sessions can even be rolled back in the case that an unintended change was made to the database. 

Some of the benefits of using an ORM are that it speeds up development time and reduces development costs by providing a much more powerful and much more efficient method of data manipulation. ORMs also provide a much simpler method of handling relationships and associations between the database entities. The mapper provides ways of defining foreign/primary keys and ways of accessing objects through related entities, allowing for very complex queries that involve dependent data to be executed much more elegantly than through straight SQL. ORMs are also intended to create a degree of portability by allowing developers to simply configure the ORM drivers/adapters to work with the database system of choice without the need to adjust any of the main program code. Another benefit of ORMs is that they provide methods for data validation and data sanitisation, by constraining data in this way it helps to add a layer of integrity to the database and prevent unwanted instances of incorrect or incomplete data being referred to. Finally ORMs promote cleaner code practice that as a result allows a greater degree of collaboration and parallel development. 


## R5 Endpoint Documentation
API Endpoint Documentation can be found here [API Endpoints](endpoints.md)

## R6 - ERD

![ERD](https://i.imgur.com/VP3gMii.jpg)

## R7 - Third Party Services
## PostgreSQL
PostgreSQL is a powerful open source database management system. Postgres utilises relational databases and allows for complex and efficient querying of large amounts of data. 

## Flask
Flask is a lightweight micro web framework for python. It allows the building and handling of URL routes and handling HTTP requests, as well as other features. Flask also supports a wide range of extensions that can further increase its functionality, such as allowing authentication, object relational mapping and encryption. 

## SQL Alchemy 
SQL Alchemy is an object relational mapper (ORM) for python. It allows for raw SQL queries to be replaced by much simpler python code. Database tables are related to python classes through SQL Alchemy allowing for complex queries to be executed easily and efficiently. 

## Marshmallow
Marshmallow is a python library that is used to serialise and deserialise data such as JSON into python data types. Marshmallow also provides methods for validation, formatting and nesting of data and objects. When used along with Flask and Python it allows for API’s to correctly handle data used in requests and responses. 

## Psycopg2
Psycopg2 is an adapter for python that allows python programs to connect to and manipulate postgres databases.  

## Bcrypt
Bcrypt is a widely used password hashing function that when used within an API allows user passwords to be securely stored encrypted and stored in a way that provides an additional layer of security. 

## JWT Manager 
JWT Manager is a python library used for handling JSON web tokens. It allows for the creation, storage, validation and management of JSON web tokens. JSON web tokens are used to authenticate users and ensure that users have the correct authorisation for certain functions within an API. 

## Python Packages
A full list of all the python packages used within this app can be found here: [python packages](requirements.txt)


## R8 - Describe your projects models in terms of the relationships they have with each other
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

## R9 - Discuss the database relations to be implemented in your application
In the proposed API webserver the database will consist of 4 main entities: Users, Games, Reviews and Comments. Users can create accounts and log in which allows them to create reviews for games and leave comments on other users reviews. Before a game can be reviewed it needs to be in the database, and only admins can create games so as to prevent any random user from creating fake games that obviously don’t exist. Following on from this brief description and by observing the above ERD the relationships between these 4 entities are simple and elegant. 

Users can create many reviews and many comments, but each review and each comment will only ever belong to a single user which means that the ‘users’ entity will be in a one-to-many relationship with both the ‘reviews’ entity and the ‘comments’ entity. As a review can have many comments and a comment will only ever be placed on a single review it means that the ‘review’ entity has a one-to-many relationship with the ‘comments’ entity. 

Finally the ‘games’ entity will only have a relationship with the ‘reviews’ entity as it is not crucial for users to have ownership over a game or for users to be able to comment on game. As a game can have many reviews but each review will only ever belong to a single game, this means that the ‘games’ entity will be in a one-to-many relationship with the ‘reviews’ entity. These are all the relationships between the entities in the database for the proposed API webserver.

## R10 Describe the way tasks are allocated and tracked in your project 
To plan and track the progress of this project Trello was used as well as participating in daily stand ups in discord. 

Link to my Trello board: https://trello.com/b/oRIZpAYq/api

I started by creating three distinct lists on trello: To-Do, In Progress, and Completed, and then populating the To-Do list with as many tasks as I could possibly think of that would be required throughout the completion of the project. Some of the cards that populated the To-Do list were comprised of smaller tasks that could be tackled one at a time until the overall task was completed, checklists were used for tasks such as these, examples below: 

![Documentation](https://i.imgur.com/kk9YABN.jpg)
![Build Models](https://i.imgur.com/T0GNcF6.jpg)
![Build Clis](https://i.imgur.com/6lgtq9n.jpg)
![Build Models](https://i.imgur.com/T0GNcF6.jpg)


## Day One

On the first day of development I wanted to just lay the foundations for the API by creating the required models, and by creating some CLI commands for populating the tables with some data. Without doing this first I would not be able to create methods for retrieving and manipulating the data in any meaningful way. I also wanted to build everything to be fully modular from the beginning but was struggling to achieve this. Initially I figured it would be easier to just build the models first, get the API working in a very rudimentary way, and then to take the very small amount of work I had created and modularise that in order to test if everything was working correctly. 

Trello after day one

![day one](https://i.imgur.com/cmdOJbn.jpg)

End of day stand up for day one

![stand up one](https://i.imgur.com/HVAtMPo.jpg)

## Day Two 
On the second day I had managed to get the very small of work I had completed fully modularised meaning that from this point it would just be a matter of simply building on top. I also managed to create a few of the CRUD routes for the simplest entity that existed at the time, the games entity. As each day passed I managed to better understand the project and what would be required, resulting in me being able to add more tasks to the To-Do section of the Trello board. 

Trello after day two

![day two](https://i.imgur.com/JA6rQ3S.jpg)

End of day stand up for day two

![stand up two](https://i.imgur.com/REExNdB.jpg)

## Day Three 
On day three I managed to make significant progress on the project overall. I finished building all of the CRUD functionality for all of the entities, added authentication and authorisation, and built and connected all of the models. I had been doing a lot of revision on the previous days, as well as building the foundations for the overall project, so by this time things started to click and become very understandable, it was just a matter of doing what I had actually set out to do. There were still a few things that were giving me some trouble. Despite having the models connected, having the necessary information with associated entities displayed correctly was quite confusing. 

Trello after day three

![day three](https://i.imgur.com/KGb31FN.jpg)

End of day stand up for day three

![stand up three](https://i.imgur.com/2iBXig5.jpg)

## Day Four
Day four was where I managed to set up a few error handlers as well as ways of validating data to be used throughout. It was important to make sure that errors were handled correctly, and that the correct data and data types were being provided and used in the database. I was still having some issues with nested information being provided properly but I felt confident that most of the functionality of the API was proceeding smoothtly, and I felt confident that I would be able to achieve what I wanted. 

Trello after day four

![day four](https://i.imgur.com/sIYLd2m.jpg)

End of day stand up for day four

![stand up four](https://i.imgur.com/IUcSB8g.jpg)

## Day Five
By day 5 I had managed to complete all of the neccesary CRUD functionality of the API, implement error handling, authorisation, authentication, and felt confident that everything was working properly. I now needed to go through all of the code and clean it up as best as I could as well as add comments explaining how all of the queries worked and what data they were intended to receive/return. As well as doing this I also decided to make a start on creating the documentation for every endpoint now that all of the endpoints had been created and tested

Trello after day five 

![day five](https://i.imgur.com/wL3cSrc.jpg)

End of day stand up for day five

![stand up five](https://i.imgur.com/Oet9oPa.jpg)


## Day Six
Day six involved finishing the the documenting of all of the endpoints as well as making some progress on the other documentation requirements. I actually made a lot more progress on this day then I thought I would. I initially planned to just tackle R1 and R2 as well as create an official ERD (the ERD I had up until then was a hand made one done on paper, and not an official one created with a computer) but after completing these tasks I felt like I had enough energy to keep pushing on and complete some of the other documentation requirements. 

Trello after day six 

![day six](https://i.imgur.com/2StSE1x.jpg)

End of day stand up for day six 

![stand up six](https://i.imgur.com/irwlKrr.jpg)

## Day Seven 
On day seven I managed to finish the rest of the documentation, and was finally able to sit back and enjoy looking at a Trello board that looks like this: 

![day seven](https://i.imgur.com/VrtQZ06.jpg)







