from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.NewsList.as_view(), name='news-list'),
    path('news/<int:pk>', views.NewsDetail.as_view(), name='news-detail'),
]
