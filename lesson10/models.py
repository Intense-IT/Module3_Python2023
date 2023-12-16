from flask_login import UserMixin

from config import db


# Добавили модели пользователя миксин для работы с авторизацией.
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    # Вместо хранения обычного пароля реализовано хранение хешированного
    hashed_password = db.Column(db.Text, nullable=False)
    address_id = db.Column(
        db.Integer, db.ForeignKey('addresses.id'), nullable=False)


class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    town_name = db.Column(db.Text, unique=True, nullable=False)
    users = db.relationship('User', backref='user_address')


# Добавили модель публикации и модель тега.
# Cвязали их между собой полем tags и атрибутом backref='posts' в модели Post.
# Для хранения данных в форме многие-ко-многим добавили
# промежуточную таблицу post_tag, а также атрибут secondary='post_tag'
# в поле tags модели Post.
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    post_name = db.Column(db.Text, nullable=False)
    tags = db.relationship('Tag', backref='posts', secondary='post_tag')


# Модель для хранения тегов
class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.Text, nullable=False)


# Промежуточная таблица, хранящая пары ключей post_id и tag_id.
# Посредством нее реализуется связь таблиц Post и Tag
# в форме многие-ко-многим.
post_tag = db.Table(
    'post_tag',
    db.Column(
        'post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column(
        'tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True),
)
