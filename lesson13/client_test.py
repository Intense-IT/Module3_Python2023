from requests import get, post, put, delete

# Запросы к списку ресурсов
# print(get('http://localhost:8080/posts').json())
# print(post(
#     'http://localhost:8080/posts',
#     json={
#         'title': 'Заголовок 2',
#         'text': 'Текст публикации 2',
#         'author_id': 3
#     }).json())


# Запросы к отдельному ресурсу
print(get('http://localhost:8080/posts/5').json())
# print(put(
#     'http://localhost:8080/posts/1',
#     json={'title': 'Изм. заголовок',
#           'text': 'Изм. текст',
#           'author_id': 5}
#           ).json())
# print(delete('http://localhost:8080/posts/1').json())
