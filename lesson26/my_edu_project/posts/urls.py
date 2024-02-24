from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(),
         name='category_detail'),
]
