from flask import render_template

from config import app, db
from models import User
from forms import UserForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    userForm = UserForm()
    if userForm.validate_on_submit():
        username = userForm.username.data
        age = userForm.age.data
        address = userForm.address.data
        user = User(username=username, age=age, address=address)
        db.session.add(user)
        db.session.commit()
    users = User.query.all()
    return render_template('users.html', form=userForm, users=users)


# Страница, где опробуем возможности фильтрации SQLAlchemy
@app.route('/spec_users', methods=['GET'])
def get_spec_users():
    userForm = UserForm()

    # get() и get_or_404() - получение объекта по первичному ключу
    user = User.query.get_or_404(1)
    print(user.username, user.address)

    # filter_by - получение списка объектов по значению поля/полей
    users = User.query.filter_by(address='Лиссабон').all()

    # filter - получение списка объектов по прописанным условиям
    users = User.query.filter(User.age > 15).all()
    users = User.query.filter(User.address == 'Лиссабон').all()
    users = User.query.filter(
        User.username.in_(['Руслан', 'Магомед', 'Шамиль'])).all()
    users = User.query.filter(User.age.in_(range(10, 30))).all()
    users = User.query.filter(User.age.not_in(range(10, 30))).all()

    # Использование логических операторов
    # and
    # Шаблон: filter(db.and_(условие1, условие2))
    users = User.query.filter(
        db.and_(
            User.age.in_(range(10, 30)),
            User.address == 'Лиссабон',
            User.username == 'Магомед'
        )
    ).all()

    # or
    # Шаблон: filter(db.or_(условие1, условие2))
    users = User.query.filter(
        db.or_(
            User.age.in_(range(10, 30)),
            User.address == 'Лиссабон',
            User.username == 'Магомед'
        )
    ).all()

    # Комбинация операторов and и or в одном фильтре
    users = User.query.filter(
        db.and_(
            db.or_(
                User.age.in_(range(10, 30)),
                User.address == 'Лиссабон'
            ),
            User.username == 'Руслан'
        )
    ).all()

    # Фильтрация по словам, оканчивающимся или начинающимся с заданной строки
    users = User.query.filter(User.username.endswith('лан')).all()
    users = User.query.filter(User.username.startswith('Са')).all()

    # order_by позволяет упорядочить набор по конкретному полю
    users = User.query.order_by(User.address).all()
    # Комбинация фильтра и сортировки
    users = User.query.filter_by(
        address='Лиссабон').order_by(User.address).all()
    # desc() - сортировка по убыванию
    users = User.query.order_by(User.address.desc()).all()
    # limit() ограничивает количество возвращаемых записей
    users = User.query.limit(1).all()

    # Обновленный синтаксис запросов для SQLAlchemy 2
    query = db.select(User).where(User.age > 10)
    users = db.session.execute(query).scalars()
    # scalars() возвращает набор из первых элементов вместо набора кортежей.
    # В нашем случае all() вместо scalars() вернет [(<User 1>,), (<User 3>,)].
    # Т.е. при вызове all() придется дополнительно вытаскивать
    # из каждого кортежа в списке первые элементы.

    return render_template('users.html', form=userForm, users=users)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8080, debug=True)
