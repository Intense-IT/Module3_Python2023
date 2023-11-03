from flask import Flask

app = Flask(__name__)


@app.route('/<string:username>', methods=['GET', 'POST'])
def index(username):
    return f'Здравствуйте, {username}'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
