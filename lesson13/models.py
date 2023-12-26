from sqlalchemy_serializer import SerializerMixin

from config import db


class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, nullable=False)
