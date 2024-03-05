from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Задание класса пагинатора на уровне отдельного представления.
    pagination_class = LimitOffsetPagination

    # Отключение пагинации для отдельного вьюсета.
    # pagination_class = None
