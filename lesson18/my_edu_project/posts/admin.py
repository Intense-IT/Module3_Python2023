from django.contrib import admin
from .models import Post, Tag, Review, Comments

# Добавляем наши модели в админку для возможности публикации записей.
admin.site.register((Post, Tag, Review, Comments))
