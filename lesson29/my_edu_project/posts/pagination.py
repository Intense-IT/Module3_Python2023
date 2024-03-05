# Пагинация, Pagination

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# Классы пагинации:
# 1. PageNumberPagination
# http://127.0.0.1:8000/posts/?page=2

# 2. LimitOffsetPagination
# http://127.0.0.1:8000/posts/?limit=100&offset=400

# 3. CursorPagination


# Создание кастомной пагинации.
class PostPagination(PageNumberPagination):
    # Количество объектов на одной странице.
    # Если установлено, переопределяет параметр PAGE_SIZE.
    page_size = 2
    # Имя параметра запроса, который позволяет клиенту устанавливать
    # количество объектов на странице для каждого запроса.
    page_size_query_param = 'page_size'
    # Максимальное количество объектов на одной странице
    # даже с учетом запроса от клиента.
    max_page_size = 100

    # Переопределение полей возвращаемого ответа пагинатора.
    def get_paginated_response(self, data):
        return Response({
            'number': self.page.paginator.count,
            'data': data,
        })
