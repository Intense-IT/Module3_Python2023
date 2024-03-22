from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, Category, Tag
from .serializers import PostSerializer, PostListSerializer, CategorySerializer
from .permissions import IsAuthorOrReadOnly
from .pagination import PostPagination


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PostPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['title', 'author']
    ordering_fields = ['title', 'pub_date']
    ordering = ['-pub_date']

    # def get_queryset(self):
    #     new_queryset = Post.objects.filter(pub_date__year__gte=2020)
    #     return new_queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostSerializer

    def get_permissions(self):
        if self.action == 'update' or self.action == 'partial_update':
            return (IsAuthorOrReadOnly(),)
        return super().get_permissions()

    @action(detail=False, methods=['get'], url_path='my_posts',
            url_name='my_posts')
    def get_my_posts(self, request) -> Response:
        posts = Post.objects.filter(author=request.user)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'],
            url_path='add_tag/(?P<tag_name>[a-z]+)', url_name='add_tag')
    def add_tag_to_post(self, request, pk=None, tag_name=None) -> Response:
        post = self.get_object()
        tag = Tag.objects.get_or_create(name=tag_name)[0]
        post.tags.add(tag)
        return Response({'message': f'Тег {tag} добавлен успешно.'})


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ['^title']


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
