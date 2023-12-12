from config import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    # Внешний ключ, указывающий на первичный ключ таблицы Address
    address_id = db.Column(
        db.Integer, db.ForeignKey('addresses.id'), nullable=False)


class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    town_name = db.Column(db.Text, unique=True, nullable=False)
    # Поле, устанавливающее связь между объектами моделей User и Address,
    # посредством которого SQLAlchemy позволяет получать
    # объекты одной модели по полям другой, связанной с ней.
    users = db.relationship('User', backref='user_address')
