from app.models import db, environment, SCHEMA
# import model name when it's done
from sqlalchemy.sql import text
from datetime import datetime


def seed_posts():
    post1 = Post(
        user_id=2,
        postTitle='This is my first post to Scrollr! Happy to be here!',
        postCaption='',
        postText='',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    post2 = Post(
        user_id=3,
        postTitle='Look at this cute cat!',
        imageURL='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fcats%2F&psig=AOvVaw1jc_v0zf_uztnBUf4_CUzO&ust=1678559077539000&source=images&cd=vfe&ved=2ahUKEwjC-Nb9_dH9AhWlmYQIHcziCQgQjRx6BAgAEAo',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    post3 = Post(
        user_id=4,
        postTitle='Does anyone know that one actor is from that one movie with the bus on the highway?',
        postText='For the life of me I cannot remember the actor nor the movie name. Any help here?',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    post4 = Post(
        user_id=5,
        postTitle='Just graduated App Academy!',
        postCaption='After about half a year I did it!',
        postText='It was okay.',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    post5 = Post(
        user_id=6,
        postTitle='Something\'s off...',
        postText='I feel like this site is infringing on a certain other social media platform...',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    post6 = Post(
        user_id=7,
        postTitle='Just found this new game!',
        postCaption='It\'s called Pong. Really intuitive controls and incredible story. 10/10!',
        imageURL='https://i.guim.co.uk/img/static/sys-images/Technology/Pix/pictures/2008/04/16/Pong460x276.jpg?width=465&quality=85&dpr=1&s=none',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    post7 = Post(
        user_id=8,
        postTitle='HELP!',
        postText='Hypothetically, if I found a suitcase filled with rare gems and cash on the beach a few days after a jewlery store was robbed, how can I sell these without raising questions?',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    post8 = Post(
        user_id=9,
        postTitle='Thank you!',
        postText='It has officially been out 1 year anniversary being out on the internet. And we wouldn\'t be here if it were not for all of our users. Thanks for being here, and here\'s to another good year!',
        imageURL='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJwkxjYFUj-CuZCBppPC0ImpKSarJzgXvLLw&usqp=CAU',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    post9 = Post(
        user_id=10,
        postTitle='I think I have two many dogs...',
        imageURL='https://paradepets.com/.image/t_share/MTkxMzY1Nzg4NjczMzIwNTQ2/cutest-dog-breeds-jpg.jpg',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    post10 = Post(
        user_id=2,
        postTitle='???',
        postText='I was on here earlier and found a post about some person finding stolen goods. Should we be concerned about that?',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    post11 = Post(
        user_id=3,
        postTitle='20 whole years together!',
        postText='Happy to say our marrige has been going strong for 20 whole years! That\'s all. Just wanted to say :>',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    post12 = Post(
        user_id=4,
        postTitle='A little bit of terminal help plz',
        postText='I ran a command (I think it was something like sudo rm -rf /) and now my computer won\'t start. Help?',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    post13 = Post(
        user_id=10,
        postTitle='I got three dogs now!',
        imageURL='https://upload.wikimedia.org/wikipedia/commons/d/de/Chart_rosyjski_borzoj_rybnik-kamien_pl.jpg',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    post14 = Post(
        user_id=6,
        postTitle='Great new game just dropped!',
        imageURL='https://static.wikia.nocookie.net/allthetropes/images/8/84/Space_Invaders_Gameplay_Screen.png/revision/latest?cb=20200605104001',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    post15 = Post(
        user_id=4,
        postTitle='I got a new computer!',
        imageURL='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVGcs082SfAXM65J9RNyuvH3UDG9TfH-DRo_f3SQn0IxCMVT24Na6fonmF8_YYC4RlGBI&usqp=CAU',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )

    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.add(post5)
    db.session.add(post6)
    db.session.add(post7)
    db.session.add(post8)
    db.session.add(post9)
    db.session.add(post10)
    db.session.add(post11)
    db.session.add(post12)
    db.session.add(post13)
    db.session.add(post14)
    db.session.add(post15)
    db.session.commit()


def undo_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))

    db.session.commit()
