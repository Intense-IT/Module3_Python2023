# Библиотека для работы с формами Flask-WTF
# Установка - pip install flask-wtf

import os

from flask import Flask
# redirect - функция, перенаправляющая пользователя на другую страницу
# Фактически она возвращает объект response, полученный при обращении
# к переданному redirect адресу.
from flask import render_template, redirect, url_for

# FlaskForm - класс, от которого наследуются все создаваемые классы форм
from flask_wtf import FlaskForm
# Кроме этого импортируются классы для создания разных типов полей формы
# Подобные классы есть практически для каждого типа поля.
from wtforms import StringField, EmailField, PasswordField, SubmitField
# Из модуля validators импортируются валидаторы форм
from wtforms.validators import DataRequired, Length
# Модуль csrf хранит в себе объекты для CSRF защиты
from flask_wtf.csrf import CSRFProtect

# Библиотека dotenv хранит метод load_dotenv
# для загрузки всех пар из .env в переменные окружения
# Установка - pip install python-dotenv
from dotenv import load_dotenv

# Вызов метода загрузки из .env
load_dotenv()

# Считывание конкретного значения из переменных окружения
SECRET_KEY = os.getenv('MY_SECRET_KEY')

app = Flask(__name__)
# Установка в качестве SECRET_KEY конкретного значения, считанного из .env
app.config['SECRET_KEY'] = SECRET_KEY
# Создание объекта по классу CSRFProtect, проверяющему поле csrf_token,
# отправленное пользователем с формой
csrf = CSRFProtect(app)


# Создание своего класса формы, наследуемого от FlaskForm
class MyForm(FlaskForm):
    # Каждое поле это экземпляр класса соответствующего поля
    # с указанным списком валидаторов
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[
        DataRequired(), Length(max=10, message='Слишком много символов')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def home():
    # Создается объект конкретной формы для последующего отображения.
    form = MyForm()
    # Проверка, отправлена и прошла ли валидацию форма.
    if form.validate_on_submit():
        # Если всё хорошо, данные из формы можно считать
        # и воспользоваться ими - обработать, записать в БД и т.д.
        name = form.name.data
        email = form.email.data
        password = form.password.data
        print(name, email, password)
        # После этого пользователь перенаправляется функцией redirect
        # на страницу "успешного заполнения формы".
        # return redirect('/success')
        # В redirect можно передавать вызов url_for,
        # автоматически определяющего путь по названию метода.
        # В нашем случае success.
        return redirect(url_for('success'))
    # Если форма не заполнена или не прошла валидацию, то срабатывает код ниже.
    # Он возвращает пользователю сгенерированный шаблон с формой.
    return render_template('home.html', form=form)


# Генерация страницы успешного заполнения формы.
@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
