# Делаем запросы к нашему приложению.
from requests import get, post


print(get('http://localhost:8080/posts').json())
print(post(
    'http://localhost:8080/posts',
    json={'text': 'Текст публикации'}).json())

# print(get('http://localhost:8080/posts/1').json())
# print(put('http://localhost:8080/posts/1', json={'name': 'Saeed'}).json())
# print(delete('http://localhost:8080/posts/1').json())
