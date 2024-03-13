from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(('posts.urls', 'posts'), namespace='posts')),

    # Подключение эндпоинтов системы аутентификации на основе сессий,
    # встроенной в DRF.
    # path('auth/', include('rest_framework.urls')),

    # Подключение эндпоинтов приложения Djoser.
    # Djoser включает в себя массу эндпоинтов для работы
    # с пользовательским классом и его аутентификацией.
    # re_path - аналог path для адресов в виде регулярных выражений.
    # re_path(r'auth/', include('djoser.urls')),
    # Подключение системы аутентификации на основе токенов, встроенной в DRF и
    # интегрированной в Djoser.
    # re_path(r'auth/', include('djoser.urls.authtoken')),

    # Подключение системы аутентификации на основе JWT.
    # Описывается два эндпоинта - для получения пары токенов access и refresh
    # и для обновления токена access посредством передачи токена refresh.
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

# При запросе на получение пары токенов на основе JWT вернулся словарь:
# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMDM0OTAzNSwiaWF0IjoxNzEwMjYyNjM1LCJqdGkiOiJjNzAwODVmYzUwYmM0Y2Y4YTA0Y2Y1YzZiMzg3YTRiMSIsInVzZXJfaWQiOjF9.NpBJLO-Rf9lqveZ1QGyYAykzU4e-zOnEU94aWjvDrWM",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMjY2NTAyLCJpYXQiOjE3MTAyNjI2MzUsImp0aSI6IjU3MjFjMTNkZGZjYTQzN2NiNjc1ODBlOWFjMmNiOGE2IiwidXNlcl9pZCI6MX0.E1fxfeoFATZ6MOamAAUt9GXIcLp95fIojNK8H8y6NoA"
# }
