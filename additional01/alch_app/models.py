from sqlalchemy import Column, Integer, String

from alch_app.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    age = Column(Integer, nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'
