from flask_login import UserMixin

from config import db


# Добавили модели пользователя миксин для работы с авторизацией.
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    # Вместо хранения обычного пароля реализовано хранение хешированного
    hashed_password = db.Column(db.Text, nullable=False)
