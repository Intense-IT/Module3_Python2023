from django.contrib import admin
from django.urls import path, include
from users.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    # Можно сделать доступными пользователю все встроенные пути
    # модуля django.contrib.auth.urls для обработки запросов авторизации.
    # path('auth/', include('django.contrib.auth.urls')),
    # Однако рекомендуетяс создание собственных обработчиков
    # на основе встроенных в django.contrib.auth.urls.
    path('', index, name='index'),
    # Подключаем все пути приложения users с префиксом auth/
    path('auth/', include('users.urls', namespace='users')),
]
