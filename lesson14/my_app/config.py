# import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    FLASK_APP = 'wsgi.py'
    # SECRET_KEY = os.getenv('SECRET_KEY')
    SECRET_KEY = 'MY_SECRET_KEY'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///my_db.db'
