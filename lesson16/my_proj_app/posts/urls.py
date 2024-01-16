from django.urls import path
from . import views


# Указываем имя приложения, которое должно совпадать с пространством имен
# в главном файле urls.py при подключении текущих URL-ов.
app_name = 'posts'

# Перечисляем все URL-ы нашего приложения posts.
urlpatterns = [
    path('', views.index),
    path('form/', views.form, name='posts_form'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<int:pk>', views.posts_detail, name='posts_detail')
]
