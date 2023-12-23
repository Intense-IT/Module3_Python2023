from sqlalchemy_serializer import SerializerMixin

from config import db


# Добавляем миксин для возможности сериалиации записей модели.
class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
