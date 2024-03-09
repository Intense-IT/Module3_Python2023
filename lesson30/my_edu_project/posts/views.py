from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Задание класса разрешения на уровне представления.
    # Встроенный класс разрешения.
    # permission_classes = (IsAuthenticated,)
    # Кастомный класс разрешения.
    permission_classes = (IsAdminOrReadOnly,)

    # get_permissions - метод, позволяющий применять различные разрешения
    # в рамках одного вьюсета.
    def get_permissions(self):
        if self.action == 'create':
            return (IsAuthorOrReadOnly(),)
        return super().get_permissions()
