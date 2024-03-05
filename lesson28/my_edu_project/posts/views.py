# Вьюсеты, ViewSet
# CBV высокого уровня, самостоятельно реализующее все базовые CRUD-операции,
# а также генерирующее необходимые эндпоинты.

# ModelViewSet - класс, реализующий все CRUD-операции с моделью.
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

# ReadOnlyModelViewSet - класс, реализующий только операции чтения с моделью,
# т.е. получение списка ресурсов и отдельного ресурса (list и retrieve).
# from rest_framework.viewsets import ReadOnlyModelViewSet

# Декоратор action позволяет создавать нестандартные представления и эндпоинты
# к текущему вьюсету.
from rest_framework.decorators import action

from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer, PostListSerializer


# Вьюсет, реализующий методы list и retrieve.
# class PostViewSet(ReadOnlyModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# Вьюсет, реализующий методы list, create, retrieve, update и destroy.
class PostViewSet(ModelViewSet):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # Добавление вьюсету нестандартного ресурса - делается с помощью
    # декоратора, которому передаются необходимые параметры.
    # Например, "methods" - перечень разрешенных методов (по умол. метод GET),
    # "detail" - взаимодействие со списком ресурсов или одиночным ресурсом,
    # и т.д.
    @action(detail=False, methods=['get'])
    # Имя метода определяет URL ресурса: posts/last_updated/
    def last_updated(self, request):
        post = Post.objects.last()
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # Метод получения класса сериализатора для представления.
    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostSerializer

    # Метод получения списка элементов для представления.
    def get_queryset(self):
        new_set = Post.objects.filter(pub_date__month__gte=3)
        return new_set


# Класс представления на основе ViewSet.
# Подразумевает обязательное определение всех необходимых методов
# (list, create, retrieve, update, partial_update, destroy).
class BasePostViewSet(ViewSet):

    def list(self, request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


# Кастомный viewset создается через GenericViewSet и миксины.
class ListCreateRetrieveUpdateViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        GenericViewSet):
    """
    Вьюсет с разрашенными методами list, create, retrieve, update.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
