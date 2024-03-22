from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PostPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 6

    def get_paginated_response(self, data) -> Response:
        return Response({
            'post_count': self.page.paginator.count,
            'posts': data
        })
