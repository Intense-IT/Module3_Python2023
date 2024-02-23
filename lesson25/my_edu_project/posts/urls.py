from django.urls import path
from . import views


# Создаем простые адреса на основе представлений от классов.
urlpatterns = [
    # path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    # path('', views.PostList.as_view(), name='post_list'),
    path('', views.PostListAPIView.as_view(), name='post_list')
]
