from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


# Adds a demo user, you can add other users here if you want
def seed_users():
    demoUser = User(
        username='Demo',
        email='demo@aa.io',
        password='password',
        profilePicUrl='',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    user2 = User(
        username='marnie',
        email='marnie@aa.io',
        password='password',
        profilePicUrl='',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    user3 = User(
        username='bobbie',
        email='bobbie@aa.io',
        password='password',
        profilePicUrl='',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    user4 = User(
        username='movieenjoyer',
        email='movies@aa.io',
        password='password',
        profilePicUrl='',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    user5 = User(
        username='danieltheprogrammer',
        email='daniel@aa.io',
        password='password',
        profilePicUrl='',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    user6 = User(
        username='normalaccount',
        email='normal@aa.io',
        password='password',
        profilePicUrl='',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    user7 = User(
        username='gameenjoyer',
        email='games@aa.io',
        password='password',
        profilePicUrl='',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    user8 = User(
        username='throwaway-account',
        email='fake@aa.io',
        password='password',
        profilePicUrl='',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    user9 = User(
        username='scrollr-official',
        email='fake@aa.io',
        password='password',
        profilePicUrl='',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    user10 = User(
        username='doglover284',
        email='dogs@aa.io',
        password='password',
        profilePicUrl='',
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )

    # 10 total accounts
    db.session.add(demoUser)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.add(user6)
    db.session.add(user7)
    db.session.add(user8)
    db.session.add(user9)
    db.session.add(user10)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
