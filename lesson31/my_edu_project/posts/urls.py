from django.urls import path

from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post-list'),
]
