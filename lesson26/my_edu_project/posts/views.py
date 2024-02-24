from rest_framework import generics
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer


# Представление для списка ресурсов публикаций
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Представление для отдельного ресурса публикаций
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Представление для отдельного ресурса категорий
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
