# Приложение для публикации новостей от имени автора с сохранением в БД
# и просмотра всех новостей конкретного автора

from flask import Flask
from flask import url_for, request
import sqlite3

app = Flask(__name__)


# Заранее создаем БД в отдельной функции
def create_table():
    con = sqlite3.connect('db/database.db')
    cursor = con.cursor()
    # cursor.execute('''DROP TABLE news;''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS news(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author TEXT,
        text TEXT
    );
    ''')
    con.commit()
    cursor.close()
    con.close()


@app.route('/')
def index():
    return 'Главная страница сайта'


# Страница публикации новостей
@app.route('/news', methods=['GET', 'POST'])
def add_news():
    if request.method == 'GET':
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Публикация новости</title>
    <link rel="stylesheet" href="{
    url_for('static', filename='css/style.css')}">
</head>
<body>
    <h1>Форма для публикации новостей</h1>
    <form action="/news" method="POST">
        <input type="text" name="username" required
        placeholder="Имя автора">
        <textarea name="news_text" cols="30" rows="10"
        placeholder="Текст публикации" required></textarea>
        <input type="submit">
    </form>
</body>
</html>'''
    else:
        con = sqlite3.connect('db/database.db')
        cursor = con.cursor()
        query = '''INSERT INTO news(author, text) VALUES(?, ?);'''
        query_data = (
            request.form.get('username'), request.form.get('news_text'))
        cursor.execute(query, query_data)
        con.commit()
        cursor.close()
        con.close()
        return 'Форма заполнена успешно.'


# Страница просмотра новостей с фильтром по автору
@app.route('/show_news', methods=['GET', 'POST'])
def show_news():
    if request.method == 'GET':
        return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
            content="width=device-width, initial-scale=1.0">
            <title>Публикация новости</title>
            <link rel="stylesheet" href="{
            url_for('static', filename='css/style.css')}">
        </head>
        <body>
            <h1>Новости авторов</h1>
            <form action="/show_news" method="POST">
                <label for="username">Внесите имя автора,
                чьи публикации хотите посмотреть.</label>
                <input type="text" name="username" name="username" required
                placeholder="Имя автора">
                <input type="submit">
            </form>
        </body>
        </html>'''
    else:
        news_text = ''
        con = sqlite3.connect('db/database.db')
        cursor = con.cursor()
        cursor.execute("""
            SELECT author, text
            FROM news
            WHERE author = ?;
        """, (request.form.get('username'),))
        news_list = cursor.fetchall()
        # Проверяем, есть ли в БД публикации данного автора
        if news_list == []:
            news_text = '<div class="no_news">К сожалению, у данного автора \
                публикаций нет.</div>'
        else:
            news_text += f'<h3>Автор статьи: \
                {request.form.get("username")}</h3>'
            for news in news_list:
                news_text += f'''
                    <article>
                        <div class='news'>{news[1]}</div>
                    </article>'''
        con.commit()
        cursor.close()
        con.close()
        return f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport"
                content="width=device-width, initial-scale=1.0">
                <title>Публикация новости</title>
                <link rel="stylesheet" href="{
                url_for('static', filename='css/style.css')}">
            </head>
            <body>
                {news_text}
            </body>
            </html>'''


if __name__ == '__main__':
    # Создаем БД перед запуском приложения
    create_table()
    app.run(host='127.0.0.1', port=8000)
