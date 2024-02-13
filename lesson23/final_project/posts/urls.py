from django.urls import path
from . import views


urlpatterns = [
    path(
        'post_detail/<int:pk>/',
        views.PostDetailView.as_view(),
        name='post_detail'
    ),
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('post_add/', views.PostAddView.as_view(), name='post_add'),
]
