# Отдельный файл, в который были вынесены модели приложения
# В ходе разработки в эти модели вносились правки, что влекло за собой
# осуществление миграций базы данных.
from config import db


class User(db.Model):
    __tablename__ = 'all_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    usersurname = db.Column(db.String(80), unique=True, nullable=True)

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(255))
