from config import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.Text, nullable=False)
