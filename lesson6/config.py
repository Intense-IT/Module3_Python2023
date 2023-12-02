# Файл конфигурации приложения, куда вынесено создание
# объектов Flask-приложения и SQLAlchemy.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db.db'

# Метаданные именования различных контрукций в скриптах миграций.
# Был добавлен, т.к. в ином случае возникала ошибка.
metadata = MetaData(
    naming_convention={
        "ix": 'ix_%(column_0_label)s',
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
)

db = SQLAlchemy(app=app, metadata=metadata)
