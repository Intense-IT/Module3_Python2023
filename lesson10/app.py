# Библиотека для работы с авторизацией пользователей Flask-Login
# pip install flask-login
from flask import render_template
# Для работы с объектом пользователя добавим модуль login_manager

# Для хеширования и проверки хеша пароля подключим функции.
# Функция создания хеша пароля.
from werkzeug.security import generate_password_hash
# Функция проверки пароля по хешу.
# from werkzeug.security import check_password_hash

from config import app, db, login_manager
from models import User, Address, Post, Tag
from forms import UserForm, AddressForm


# Callback (обратный вызов) используется для перезагрузки объекта пользователя
# по идентификатору пользователя, хранящемуся в сеансе.
@login_manager.user_loader
def load_user(user_id):
    db_sess = db.session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    users = User.query.all()

    # Для проверки возможности добавлять отношения многие-ко-многим пропишем
    # ряд команд.
    # Добавим несколько объектов публикаций и тегов.
    post1 = Post(post_name='Название1')
    post2 = Post(post_name='Название2')
    db.session.add(post1)
    db.session.add(post2)
    tag1 = Tag(tag_name='Тег1')
    tag2 = Tag(tag_name='Тег2')
    db.session.add(tag1)
    db.session.add(tag2)

    # Сохраним в переменные объекты тегов, найденные по запросу.
    post1 = Post.query.get_or_404(4)
    tag1 = Tag.query.get_or_404(1)
    tag2 = Tag.query.get_or_404(2)

    # Добавим первой публикации оба тега
    post1.tags.append(tag1)
    post1.tags.append(tag2)

    # Убедимся, что список тегов хранится в объекте публикаций
    # и список публикации хранится в объекте тегов.
    print(post1.tags)
    print(tag1.posts)
    print(tag2.posts)

    db.session.commit()
    return render_template('index.html', users=users)


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    userForm = UserForm()
    if userForm.validate_on_submit():
        username = userForm.username.data
        password = userForm.password.data
        # Считанное с формы значение пароля захешируем.
        hashed_password = generate_password_hash(password)
        address = userForm.address.data
        # Создадим объект пользователя с хешем вместо пароля.
        user = User(
            username=username,
            hashed_password=hashed_password,
            address_id=address
            )
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


# Обработчик ошибки 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


# Обработчик ошибки 403
@app.errorhandler(403)
def not_permitted(error):
    return render_template('403.html', error=error), 403


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8080, debug=True)
