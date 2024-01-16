"""Это файл, хранящий основные URL-ы проекта.
Как правило, URL-ы приложений подключаются к данному файлу разом,
сразу всем набором URL-ов отдельного приложения.
"""

from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('greet/<str:name>', views.greet, name='greet')
    path('greet', views.greet, name='greet')
]
