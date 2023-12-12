# Данное приложение нацелено на демонстрацию возможностей SQLAlchemy
# в создании связей между таблицами, а именно один-ко-многим (one-to-many).
# Для этого ключевые изменения вносятся в структуру моделей.
# После можно использовать связь один-ко-многим для упрощения запросов.

from flask import render_template

from config import app, db
from models import User, Address
from forms import UserForm, AddressForm


# На главной странице будем отображать список пользователей,
# а также использовать ее как способ вызова функции для ORM-команд.
@app.route('/')
def index():
    users = User.query.all()

    # Обычный способ создания объекта записи пользователя с id адреса,
    # взятым из таблицы адресов через filter_by().
    town = Address.query.filter_by(town_name='Махачкала').first()
    user = User(username='Магомед', address_id=town.id)
    print(user.username, user.address_id)

    # Добавим несколько записей в таблице Address.
    town1 = Address(town_name='Каспийск')
    town2 = Address(town_name='Дербент')
    db.session.add(town1)
    db.session.add(town2)
    # Добавим несколько записей в таблице User,
    # в качестве внешнего ключа address_id у которых
    # указан id созданной записи в таблице Address.
    user1 = User(username='Гасей', address_id=2)
    user2 = User(username='Сидредин', address_id=2)
    db.session.add(user1)
    db.session.add(user2)

    # В модель Address добавлено поле users типа relationship.
    # Теперь при желании мы можем получить у любого объекта таблицы Address
    # список всех объектов пользователей, которые указывают на объект Address
    # через поле users.
    address = Address.query.get(2)
    # Выведем всех пользователей, проживающих в городе address.
    for user in address.users:
        print(user.username)

    # Кроме того, посредством атрибута backref поля users в таблице Address
    # мы добавили таблице User дополнительный указатель user_address,
    # через который можно получить объект таблицы Address,
    # на который указывает внешний ключ записи в таблице User.
    user2 = User.query.get(2)
    # Выведем название города, где проживает пользователь user2.
    print(user2.user_address.town_name)

    db.session.commit()
    return render_template('index.html', users=users)


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    userForm = UserForm()
    if userForm.validate_on_submit():
        username = userForm.username.data
        address = userForm.address.data
        user = User(username=username, address_id=address)
        db.session.add(user)
        db.session.commit()
    users = User.query.all()
    return render_template('users.html', form=userForm, users=users)


@app.route('/towns', methods=['GET', 'POST'])
def get_towns():
    addressForm = AddressForm()
    if addressForm.validate_on_submit():
        town_name = addressForm.town_name.data
        town = Address(town_name=town_name)
        db.session.add(town)
        db.session.commit()
    towns = Address.query.all()
    return render_template('towns.html', form=addressForm, towns=towns)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8080, debug=True)
