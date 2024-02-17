from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PostList.as_view(), name='post_list'),
]
