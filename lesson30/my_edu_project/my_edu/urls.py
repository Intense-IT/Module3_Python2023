from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(('posts.urls', 'posts'), namespace='posts')),

    # Подключение эндпоинтов системы аутентификации на основе сессий,
    # встроенной в DRF.
    # path('auth/', include('rest_framework.urls')),

    # Подключение эндпоинтов приложения Djoser.
    path(r'auth/', include('djoser.urls')),
    # Подключение системы аутентификации на основе токенов, встроенной в DRF и
    # интегрированной в Djoser.
    path(r'auth/', include('djoser.urls.authtoken')),
]
