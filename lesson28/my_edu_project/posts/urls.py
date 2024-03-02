# URL-ы вьюсетов
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework.routers import SimpleRouter
from . import views

# Класс SimpleRouter генерирует эндпоинты списка ресурсов
# и отдельного ресурса для зарегистрированного вьюсета.
# router = SimpleRouter()

# Класс DefaultRouter работает аналогично SimpleRouter, однако
# дополнительно включает дефолтное корневое API представление,
# возвращающее ответ с гиперссылками на все представления списка.
router = DefaultRouter()

# Все представления и эндпоинты регистрируются в роутере.
# В качестве URL-адреса применяется регулярное выражение.
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    # Полученный router в итоге добавляется в urlpatterns.
    path('', include(router.urls)),
]
