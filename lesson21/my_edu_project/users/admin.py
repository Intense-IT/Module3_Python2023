from django.contrib import admin
from .models import CustomUser


# Для возможности работать в админке с записями кастомной модели пользователей
# необходимо явно ее добавить.
admin.site.register(CustomUser)
