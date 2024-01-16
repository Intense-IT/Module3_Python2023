from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_login import LoginManager


db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes

        return app
