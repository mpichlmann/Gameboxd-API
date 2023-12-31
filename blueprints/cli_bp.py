from flask import Blueprint
from datetime import date
from models.comment import Comment
from models.user import User
from models.game import Game
from models.review import Review
from init import db, bcrypt


cli_bp = Blueprint('db', __name__)

@cli_bp.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print('Tables created successfully')

@cli_bp.cli.command('seed')
def seed_db():
    #Seed Games
    games = [
        Game(
            title = 'Elden Ring',
            genre = 'RPG',
            description = 'Explore an open world, become Elden Lord and unite the Elden Ring!',
            platforms = 'Playstation, Xbox, PC'
        ),
        Game(
            title = 'Resident Evil 4 Remake',
            genre = 'Horror',
            description = 'Survive monsters and horrors, and stop an evil plot',
            platforms = 'Playstation, Xbox, PC'
        ),
        Game(
            title = 'Luigis Mansion 3',
            genre = 'Action-Adventure',
            description = 'Clean up the ghosts with your buddy Gooigi and save Mario in a haunted hotel',
            platforms = 'Nintendo Switch'
        ),
        Game(
            title = 'Overcooked 2',
            genre = 'Party-Puzzle',
            description = 'Dish up as fast as you can without getting orders wrong!',
            platforms = 'PC, Playstation, Xbox, Nintendo Switch'
        )
    ]
    db.session.query(Game).delete()
    db.session.add_all(games)
    db.session.commit()

    #Seed Users
    users = [
        User(
            name = 'Adam Minister',
            email = 'admin@gameboxd.com',
            password = bcrypt.generate_password_hash('password123').decode('utf-8'),
            is_admin = True
        ),
        User(
            name = 'Jay Son',
            email = 'jayson@test.com',
            password = bcrypt.generate_password_hash('testpass123').decode('utf-8')
        ),
        User(
            name = 'Queen Boo',
            email = 'queenboo@mansion.com',
            password = bcrypt.generate_password_hash('scaryboo').decode('utf-8'),
            is_admin = True,
        ),
        User(
            name = 'Post Man',
            email = 'postman@post.com',
            password = bcrypt.generate_password_hash('postmanpass').decode('utf-8')
        ),
        User(
            name = 'Mario Brutha',
            email = 'mushroom@kingdom.com',
            password = bcrypt.generate_password_hash('princesspeach').decode('utf-8')
        ),
        User(
            name = 'Edward Scissorhands',
            email = 'Burton@Hollywood.com',
            password = bcrypt.generate_password_hash('HedgeTrimmer').decode('utf-8')
        ),
    ]
    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()

    #Seed Reviews
    reviews = [
        Review(
            title = 'FromSoftwares latest masterpiece',
            rating = 5,
            body = 'the game is awesome, I loved it! Incredible world design and combat encounters',
            date_created = date.today(),
            user_id = users[0].id,
            game_id = games[0].id
        ),
        Review(
            title = 'RE4 leaves a lot to be desired',
            rating = 3,
            body = 'Its okay, not amazing, not awful. The gameplay is a little dated',
            date_created = date.today(),
            user_id = users[1].id,
            game_id = games[1].id           
        ),
        Review(
            title = 'Not the high water mark for FromSoftware',
            rating = 2,
            body = 'Elden ring is nowhere near as good as FromSoftwares other games, Sekiro has the better combat and dark souls has the better atmosphere 100%',
            date_created = date.today(),
            user_id = users[2].id,
            game_id = games[0].id           
        ),
        Review(
            title = 'Easily my favourite game on the switch',
            rating = 5,
            body = 'The best game on the Switch by far. Great atomsphere, story, and level design. This game suprises you and has a lot of variety. It is a near perfect game and my all time favourite, but my only crtiscm is that there is a lot of currency in the game but almost nothing to spend it on. Some cute outfits for myself and Gooigi would have been cool. Other than that, this game is the best. Highly reccomend, must have for the switch.',
            date_created = date.today(),
            user_id = users[2].id,
            game_id = games[2].id           
        ),
        Review(
            title = 'A modern masterpiece',
            rating = 5,
            body = 'Capcom has done it again. Following the success of their remasters of Resident Evil 2 and Resident Evil 3, this latest release is nothing short of perfection. Resident Evil 4 is loving remastered for modern audiences. The game has been tailored to perfection.',
            date_created = date.today(),
            user_id = users[3].id,
            game_id = games[1].id           
        ),
        Review(
            title = 'I was too scared to finish the game',
            rating = 4,
            body = 'As the title says, I found this game way too scary to even finish! The game is good dont get me wrong, in fact it is TOO good!!',
            date_created = date.today(),
            user_id = users[4].id,
            game_id = games[1].id           
        )
    ]
    db.session.query(Review).delete()
    db.session.add_all(reviews)
    db.session.commit()

    #Seed Comments
    comments = [
        Comment(
        body = 'I agree, elden ring is a fantastic game',
        date_created = date.today(),
        user_id = users[1].id,
        review_id = reviews[0].id
        ),
        Comment(
        body = 'I disagree, I think RE4 is a fantastic modern remake',
        date_created = date.today(),
        user_id = users[0].id,
        review_id = reviews[1].id
        ),
        Comment(
        body = 'Maybe you should get good? Elden Ring is game of the year',
        date_created = date.today(),
        user_id = users[3].id,
        review_id = reviews[2].id
        ),
        Comment(
        body = 'I also love Luigis Mansion 3, best game ever!',
        date_created = date.today(),
        user_id = users[0].id,
        review_id = reviews[3].id
        )
        ,
        Comment(
        body = 'Resident evil 4 sucks, the original is way better',
        date_created = date.today(),
        user_id = users[4].id,
        review_id = reviews[4].id
        )
        ,
        Comment(
        body = 'I LOVE LUIGI!!!',
        date_created = date.today(),
        user_id = users[4].id,
        review_id = reviews[3].id
        )
        ,
        Comment(
        body = 'I think you are missing what makes Elden Ring such an impressive game. The sheer scale and diversity of the world is something to be awed by.',
        date_created = date.today(),
        user_id = users[0].id,
        review_id = reviews[2].id
        )
    ]
    db.session.query(Comment).delete()
    db.session.add_all(comments)
    db.session.commit()

    
    
    print('tables seeded')