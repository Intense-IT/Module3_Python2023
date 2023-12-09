from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db.db'

db = SQLAlchemy(app=app)

# Перенесли настройки csrf из app.pys
SECRET_KEY = 'Мой секретный ключ'
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)
