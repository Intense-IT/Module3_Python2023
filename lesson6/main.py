# Миграции - инструмент для изменения структуры уже имеющейся базы данных.
# Библиотека Flask-Migrate, основывается на библиотеке Alembic.
# pip install Flask-Migrate

from flask import redirect, render_template, request, url_for
# Импортируем класс Migrate из установленной библиотеки.
from flask_migrate import Migrate

from config import app, db
from models import User, Post

# Инициализация Flask-Migrate в главном скрипте main.py
# с Flask-приложением и экземпляром SQLAlchemy.
migrate = Migrate(app, db)


# Т.к. наше flask-приложение незнакомо терминалу, выполним в терминале:
# export FLASK_APP=main
# Вместо main укажите название вашего главного скрипта.


# Инициализация миграций
# Для инициализации миграций и создания директории с файлами
# модификации БД в терминале необходимо ввести команду:
# flask db init
# В результате появится папка migrations с целым набором рабочих файлов
# При возникновении ошибки можно попробовать модифицировать команду:
# python -m flask db init


# Создание скрипта миграций
# Для создания скрипта, содержащего информацию об алгоритме миграций
# по внесенным изменениям в БД введите команду, указав свое сообщение:
# flask db migrate -m "сообщение к миграции"
# В результате в папке versions появится файл с id и вашим сообщением,
# где будет описана последовательность действий для миграции.
# В саму базу данных на данном этапе никаких изменений не вносит.
# При необходимости в файл можно внести правки.
# При возникновении ошибки можно попробовать модифицировать команду:
# python -m flask db migrate -m "сообщение к миграции"


# Выполнение миграций
# Для применения миграций к нашей БД выполните команду:
# flask db upgrade
# Данная команда выполняет скрипт миграций и применяет изменения к БД.
# При возникновении ошибки можно попробовать модифицировать команду:
# python -m flask db upgrade


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get('username')
    usersurname = request.form.get('usersurname')
    user = User(username=username, usersurname=usersurname)
    db.session.add(user)
    db.session.commit()
    print(user.id, user.username)
    return redirect(url_for('index'))


@app.route('/posts', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form.get('title')
        text = request.form.get('text')
        post = Post(title=title, text=text)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('add_post'))
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8080, debug=True)
