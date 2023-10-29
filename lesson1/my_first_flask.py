# Установка Flask
# pip install flask

# Этапы развития
# CGI -> WSGI -> Werkzeug и Jinja2 -> Flask


# Создаем простое приложение на Flask
# Импортирум класс для создания объекта приложения
from flask import Flask
from flask import request  # не путать с библиотекой requests

app = Flask(__name__)  # создается объект приложения


# Главная страница
@app.route('/')  # декоратор, связывающий URL и функцию
@app.route('/index')
def hello_world():  # функция, вызываемая при обращении к URL
    return 'Hello, World!'  # Flask преобразует строку в объект ответа


# Страница /about
@app.route('/about')
def about_us():
    text = 'Меня зовут Саид.<br>'
    return text * 5


# Страница /news
@app.route('/news')
def news_text():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Новость</title>
    <style>h1 {color: red;}</style>
</head>
<body>
    <h1>Новость</h1>
    <div>Lorem ipsum dolor sit amet consectetur adipisicing elit.
    Soluta eligendi, nam provident expedita voluptas exercitationem ad fuga
    voluptatem harum facere ipsum nisi quod asperiores similique alias dolore,
    laborum magnam error.</div>
</body>
</html>'''


# В URL можно задавать динамический параметр, передающий информацию
# из адресной строки пользователя в функцию
@app.route('/users/<username>')
def show_user(username):
    return f'Пользователь с id {username}'


# Можно явно обозначить тип параметра
# Наиболее часто используются типы int, float, string
@app.route('/posts/<int:id>')
def show_post(id):
    return f'Публикация № {id}'


# Можно явно задавать принимаемые запросы в форме списка
# По умолчанию разрешен только метод GET
@app.route('/login', methods=['GET', 'POST'])
def login():
    # В зависимости от типа запроса возвращаем разный контент
    if request.method == 'GET':
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
    else:
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Авторизация</title>
</head>
<body>
    <div>Поздравляю, вы авторизировались</div>
</body>
</html>''', 201


if __name__ == '__main__':
    # Приложение запускается командой app.run()
    # app.run(debug=True)  # приложение можно запустить в режиме отладки
    # Можно явно указать ip и порт запуска приложения
    app.run(host='127.0.0.1', port=8000)
