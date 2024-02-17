# DRF-представления на основе классов
from rest_framework import generics
from rest_framework import permissions

from .models import Post
from .serializers import PostSerializer


# Представление для списка ресурсов
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Представление для отдельного ресурса
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated)
