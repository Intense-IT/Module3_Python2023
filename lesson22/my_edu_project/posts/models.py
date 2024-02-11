from django.db import models


# Простая модель для демонстрации работы CBV.
class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()


# Для добавления записей без применения админки сайта
# вызовем в терминале оболочку Django (shell).
# python manage.py shell

# Сначала импортируем модель Post.
# from posts.models import Post
# Далее создаем нужное количество записей командой create.
# Post.objects.create(title='Заголовок', text='Текст')
