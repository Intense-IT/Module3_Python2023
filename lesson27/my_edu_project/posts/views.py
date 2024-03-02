# ПРЕДСТАВЛЕНИЯ В DRF

from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework import generics, mixins
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


# Представления на основе функций
# Нужной функции задается декоратор api_view с разрешенными методами.
@api_view(['GET', 'POST'])
def index(request):
    """
    Главная страница.
    """
    if request.method == 'POST':
        return Response({'message': 'Получены данные', 'data': request.data})
    return Response({'message': 'Главная страница!'})

# Функция для работы со списком ресурсов.
# @api_view(['GET', 'POST'])
# def post_list(request):
#     '''
#     Получаем список публикаций или создаем новую.
#     '''
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(author=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Функция для работы с отдельным ресурсом.
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def post_detail(request, pk):
#     '''
#     Получаем, изменяем или удаляем отдельную публикацию.
#     '''
#     # post = Post.objects.get(pk=pk)
#     post = get_object_or_404(Post, pk=pk)

#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'PUT' or request.method == 'PATCH':
#         # аргумент partial позволяет передавать не все аргументы,
#         # отсутствие обязательных полей не вызовет ошибку.
#         serializer = PostSerializer(
#             post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------------------------------------------------------------------
# Представления на основе классов
# Структура классов представлений в DRF:
# https://www.cdrf.co/


# ---------------------------------------------------------------------------
# Класс APIView
# Предоставляет возможность определять запросы посредством одноименных методов.
# Класс для работы со списком ресурсов.
# class APIPostList(APIView):
#     '''
#     Получаем список публикаций или создаем новую.
#     '''
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(author=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Класс для работы с отдельным ресурсом.
# class APIPostDetail(APIView):
#     '''
#     Получаем, изменяем или удаляем отдельную публикацию.
#     '''
#     def get(self, request, pk=None):
#         post = get_object_or_404(Post, pk=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk=None):
#         post = get_object_or_404(Post, pk=pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk=None):
#         post = get_object_or_404(Post, pk=pk)
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk=None):
#         post = get_object_or_404(Post, pk=pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------------------------------------------------------------------
# GenericAPIView и миксины (примеси).
# Классы представлений формируются на основе базового класса GenericAPIView
# и добавления миксинов с необходимым функционалом.
# Список миксинов:
# - ListModelMixin
# - CreateModelMixin
# - RetrieveModelMixin
# - UpdateModelMixin
# - DestroyModelMixin

# Класс для работы со списком ресурсов.
# class PostList(mixins.ListModelMixin,
#                mixins.CreateModelMixin,
#                generics.GenericAPIView):
#     '''
#     Получаем список публикаций или создаем новую.
#     '''
#     # queryset и serializer_class обеспечиваются классом GenericAPIView.
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     # Метод list обеспечивается миксином ListModelMixin
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # Метод create обеспечивается миксином CreateModelMixin
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# Класс для работы с отдельным ресурсом.
# class PostDetail(mixins.RetrieveModelMixin,
#                  mixins.UpdateModelMixin,
#                  mixins.DestroyModelMixin,
#                  generics.GenericAPIView):
#     '''
#     Получаем, изменяем или удаляем отдельную публикацию.
#     '''
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     # Метод retrieve обеспечивается миксином RetrieveModelMixin
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     # Метод update обеспечивается миксином UpdateModelMixin
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     # Метод partial_update обеспечивается миксином UpdateModelMixin
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

#     # Метод destroy обеспечивается миксином DestroyModelMixin
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# ---------------------------------------------------------------------------
# Дженерики - встроенные классы, наследующие функционал от GenericAPIView
# и миксинов в разных комбинациях.
# В случае дженериков достаточно задать поля без определения методов.
# Однако при необходимости всегда можно переопределить любой из методов.
# Список дженериков:
# - ListAPIView
# - CreateAPIView
# - ListCreateAPIView
# - RetrieveAPIView
# - UpdateAPIView
# - DestroyAPIView
# - RetrieveUpdateAPIView
# - RetrieveDestroyAPIView
# - RetrieveUpdateDestroyAPIView

# Класс для работы со списком ресурсов.
class PostList(generics.ListCreateAPIView):
    '''
    Получаем список публикаций или создаем новую.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # При необходимости здесь же задаются другие атрибуты,
    # будь то класс пагинации или используемые фильтры/сортировки
    # (pagination_class, filter_backends и т.д.).

    # При необходимости в дженериках можно переопределить методы,
    # связанные с созданием, обновлением или удалением ресурса:
    # perform_create, perform_update, perform_destroy.
    # В примере ниже мы при сохранении в БД сериализованных данных добавляем
    # текущего пользователя в качестве автора.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Класс для работы с отдельным ресурсом.
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Получаем, изменяем или удаляем отдельную публикацию.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
