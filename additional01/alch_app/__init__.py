from flask import Flask
from sqlalchemy import select

from alch_app.db import session
from alch_app.models import User


app = Flask(__name__)


@app.route('/')
def index():
    # CREATE
    new_user = User(username='user1', email='user1@mail.ru')
    session.add(new_user)
    session.commit()

    # READ
    user1 = session.get(User, 1)
    print(user1)
    user2 = session.execute(
        select(User).filter_by(username='user1')).scalar_one()
    print(user2)

    users = session.execute(select(User).order_by(User.username)).scalars()
    for elem in users:
        print(elem)

    # UPDATE
    user = session.execute(
        select(User).filter_by(username='user1')).scalar_one()
    user.email = 'user2@yandex.ru'
    session.commit()

    # DELETE
    user = session.execute(
        select(User).filter_by(username='user1')).scalar_one()
    session.delete(user)
    session.commit()

    return 'SQLAlchemy works!'
