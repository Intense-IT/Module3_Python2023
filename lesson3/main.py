# Шаблонизация, jinja2

from flask import Flask
# render_template позволяет рендерить html из шаблона
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    # params - словарь, в который мы занесем все значения для передачи шаблону.
    # В самом шаблоне можно получить значение через точечную нотацию.
    # Например: params.name или params.surname
    params = {}
    params['name'] = 'Qwerty'
    params['surname'] = 'Амиров'
    # render_template принимает 1 позиционный аргумент, название шаблона,
    # и любое количество именованных аргументов.
    return render_template('home.html', params=params)


@app.route('/about')
def about():
    # Функции render_template можно передавать и списки
    staff = ['Магомед', 'Патимат', 'Сидредин']
    return render_template('about.html', staff=staff)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
