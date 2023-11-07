# Приложение на повторение темы шаблонизация
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', username='Магомед')


if __name__ == '__main__':
    app.run()
