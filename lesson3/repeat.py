# Повторение тем статические файлы и обработка форм
from flask import Flask
from flask import url_for, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="
    {url_for('static', filename='css/style.css')}">
</head>
<body>
    <div>Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    Vel earum, dolor libero dolores, in asperiores rerum repellendus
    voluptates deserunt ex molestias ab nesciunt! Corrupti tempore accusantium
    omnis, quos facere odit.</div>
    <form action="/" method="POST">
        <input type="text" name="text" id="tex">
        <input type="submit">
    </form>
</body>
</html>'''
    else:
        return f'{request.form.get("text")}'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
