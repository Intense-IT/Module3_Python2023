from flask import render_template, request
from flask_migrate import Migrate

from flask_wtf.csrf import CSRFProtect

from config import app, db
from models import Post, Author
from forms import PostForm, AuthorForm

migrate = Migrate(app, db)
# Команды для миграции:
# flask db init
# flask db migrate -m "сообщение к миграции"
# flask db upgrade

SECRET_KEY = 'Мой секретный ключ'
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


# Работа со страницей posts, содержащей форму и список публикаций
@app.route('/posts', methods=['GET', 'POST'])
def add_post():
    postForm = PostForm()
    if request.method == 'POST':
        if postForm.validate_on_submit():
            title = postForm.title.data
            text = postForm.text.data
            author = postForm.author.data
            post = Post(title=title, text=text, author=author)
            db.session.add(post)
            db.session.commit()
    posts = Post.query.all()
    return render_template('posts.html', posts=posts, form=postForm)


# Работа со страницей отдельной формы
@app.route('/posts/<int:post_id>')
def get_post(post_id):
    # get() - метод для получения отдельной публикации по первичному ключу.
    # post = Post.query.get(post_id)

    # get_or_404() - безопасная форма метода get()
    # Вызывает ошибку 404 в случае проблем отсутствия объекта.
    post = Post.query.get_or_404(post_id)
    return render_template('single_post.html', post=post)


# Работа со страницей публикаций автора
@app.route('/posts/author/<string:author_name>')
def get_author_posts(author_name):
    # filter_by() - позволяет отфильтровать записи по значению поля/полей.
    # first() - метод, возвращающий первую публикацию в отфильтрованном наборе.
    # posts = Post.query.filter_by(author=author_name).first()

    # first_or_404() - безопасная форма метода first().
    # posts = Post.query.filter_by(author=author_name).first_or_404()
    posts = Post.query.filter_by(author=author_name).all()
    return render_template('author_posts.html', posts=posts)


# Работа со страницей списка всех авторов, подходящих по условию
@app.route('/authors', methods=['GET', 'POST'])
def get_authors():
    authorForm = AuthorForm()
    if request.method == 'POST':
        if authorForm.validate_on_submit():
            username = authorForm.username.data
            age = authorForm.age.data
            bio = authorForm.bio.data
            author = Author(username=username, age=age, bio=bio)
            db.session.add(author)
            db.session.commit()

    # Отображаем только авторов, чей возраст больше 20
    # Для этого воспользуемся методом запросов filter(),
    # который позволяет использовать условные конструкции.
    authors = Author.query.filter(Author.age > 20).all()
    return render_template('authors.html', authors=authors, form=authorForm)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8080, debug=True)
