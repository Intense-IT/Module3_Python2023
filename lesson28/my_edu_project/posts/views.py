# Вьюсеты, ViewSet
# CBV высокого уровня, самостоятельно реализующее все базовые CRUD-операции,
# а также генерирующее необходимые эндпоинты.

# ModelViewSet - класс, реализующий все CRUD-операции с моделью.
from rest_framework.viewsets import ModelViewSet

# ReadOnlyModelViewSet - класс, реализующий только операции чтения с моделью,
# т.е. получение списка ресурсов и отдельного ресурса (list и retrieve).
# from rest_framework.viewsets import ReadOnlyModelViewSet

# Декоратор action позволяет создавать нестандартные представления и эндпоинты
# к текущему вьюсету.
from rest_framework.decorators import action

from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


# Вьюсет, реализующий методы list и retrieve.
# class PostViewSet(ReadOnlyModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# Вьюсет, реализующий методы list, create, retrieve, update и destroy.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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
