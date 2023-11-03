# Добавление статического контента на сайт
# Обработка полей форм

from flask import Flask
# Для добавления статического контента понадобится функция url_for
# request необходим для получения данных из формы
from flask import url_for, request


app = Flask(__name__)

USERS = {'Saeed': '12345', 'Magomed': 'qwer12'}


@app.route('/')
def index():
    return 'Здравствуйте'


# Страница news, где размещается новость, снабжена CSS-стилями и изображением
# Сам статический контент располагается в папке static
@app.route('/news')
def news():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Новость</title>
    <link rel="stylesheet" href="{
        url_for('static', filename='css/style.css')}">
</head>
<body>
    <h1>Новость</h1>
    <div>Lorem, ipsum dolor sit amet consectetur adipisicing elit.
        Porro totam id repudiandae deserunt saepe placeat eius illum?
        Voluptates quae numquam ipsam ea reprehenderit iste saepe
        totam beatae maiores. Velit, minus.</div>
    <img src="{url_for('static', filename='img/cat.jpg')}" alt="">
</body>
</html>'''


# Страница login позволяет заполнять форму и обрабатывать переданные значения
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form.get('login'))
        # print(request.form.get('pass'))
        if USERS[request.form.get('login')] == request.form.get('pass'):
            return 'Форма заполнена успешно'
        return 'Пароль неверный!'
    else:
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Авторизация</title>
</head>
<body>
    <!-- По умолчанию форма присылает GET-запросы,
    но нам нужен POST-запрос -->
    <form action="/login" method="POST">
        <input type="text" name="login" required>
        <input type="password" name="pass" required>
        <input type="submit">
    </form>
</body>
</html>'''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
