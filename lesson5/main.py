# ORM - инструмент, предоставляющий возможность работать с БД
# через объекты, превращая высокоуровневые операции в SQL-команды БД.

# SQLAlchemy управляет связыванием таблиц и моделей,
# а также очисткой соединений и сеансов после каждого запроса.
# pip install Flask-SQLAlchemy

from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Сохраняем URI нашей БД, указав ее название.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db.db'
# Создаем объект
db = SQLAlchemy(app)


# Создадим модели нашей БД как классы.
# Каждый класс представляет отдельную таблицу в БД.
# Модель User для хранения данных о пользователях.
class User(db.Model):
    # Имя таблицы устанавливается автоматически из названия класса модели.
    # При желании можно задать конкретное название через свойство __tablename__
    __tablename__ = 'all_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
# Распространенные типы - Integer, String, Text, Boolean, DateTime,
# Float, LargeBinary

    # Для настройки отображения технических данных об объекте класса
    # можно переназначить метод __repr__.
    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"


# Модель Post для хранения данных о публикациях.
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(255))


# Главная страница со списком пользователей и формой
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


# Роутер для обработки POST-запросов на добавление пользователя.
@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get('username')
    # Создаем объект-запись - экземпляр модели User
    user = User(username=username)
    # Добавляем запись в БД
    db.session.add(user)
    # Подтверждаем изменения.
    db.session.commit()
    # При необходимости можем обратиться к полям записи через свойства объекта
    print(user.id, user.username)
    return redirect(url_for('index'))


# Роутер для отображения и обработки запросов на добавление публикаций.
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
    # Для создания всех таблиц в БД используется конструкция нижи.
    # Она выполняется в случае, если таблицы не созданы.
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8080, debug=True)
