# Создание RESTful API на Flask
# pip install Flask-RESTful
# pip install SQLAlchemy-serializer

from flask import jsonify, request
# Подключаем родительский класс для создания классов ресурсов.
from flask_restful import Resource

from config import app, api, db
from models import Post


# Для операций над ресурсами создается два класса ресурсов,
# описывающих операции над объектами определенного ресурса.
# Ниже представлены оба класса для ресурса Post.

# Класс для управления списком объектов.
class PostListResource(Resource):
    # Метод получения списка объектов публикаций
    def get(self):
        posts = Post.query.all()
        # Использованный раньше response со списком.
        # return render_template('posts.html', posts=posts)
        # Создание ответа с применением сериализатора.
        return jsonify(
            {
                'posts': [
                    post.to_dict(only=('text',))
                    for post in posts
                ]
            }
        )

    # Метод добавления объекта публикации
    def post(self):
        data1 = request.json
        post = Post(text=data1['text'])
        db.session.add(post)
        db.session.commit()
        # Создание ответа с применением сериализатора.
        # return jsonify({'success': 'OK'})
        return jsonify(
            {
                'posts': post.to_dict(only=('text',))
            }
        )


# Класс для управления отдельным объектом.
class PostResource(Resource):
    # Получение отдельного объекта статьи
    def get(self, post_id):
        return {'message': f'Get {post_id}'}

    # Замена существующего объекта статьи
    def put(self, post_id):
        return {'message': f'Put {post_id}'}

    # Удаление объекта статьи
    def delete(self, post_id):
        return {'message': f'Delete {post_id}'}


# Добавление данных о классах и соответствующих им URL в API.
api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run('127.0.0.1', 8080)
