from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db.db'

db = SQLAlchemy(app)
# Подключаем restful к нашему приложению.
api = Api(app)
