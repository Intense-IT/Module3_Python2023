# Миграции необходимо делать при каждом изменении модели.
# Кроме того, на старте работы над проектом необходимо провести
# базовые миграции для встроенных моделей Django.
# python manage.py migrate

# Команда создания скрипта с описанием алгоритма миграций
# python manage.py makemigrations
# Рекомендуется явно указывать в команде приложение,
# для которого генерируется скрипт миграций:
# python manage.py makemigrations posts
# Все скрипты миграций фиксируются в папках migrations каждого приложения.

# После создания скрипта миграций проведем сами миграции -
# изменения в базе данных по изменениям, сделанным в моделях:
# python manage.py migrate

from django.db import models
from django.contrib.auth import get_user_model


RATING = [(1, 'Плохо'), (2, 'Посредственно'), (3, 'Нормально'), (4, 'Хорошо')]


# Получаем встроенную модель пользователя.
User = get_user_model()


# Модель тегов
class Tag(models.Model):
    name = models.CharField(max_length=15, unique=True, null=False)


# Модель публикаций
class Post(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        help_text='Заголовок'
    )
    text = models.TextField(blank=False, help_text='Текст')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        help_text='Автор'
    )
    # Посредством поля tags реализуем связь Многие-ко-многим с моделью Tag.
    tags = models.ManyToManyField(
        Tag,
        related_name='posts',
        through='PostTag',
        help_text='Теги'
    )

    class Meta:
        ordering = ['-pub_date']


# Промежуточная модель для связи Многие-ко-многим моделей Post и Tag
class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


# Модель комментариев
class Comments(models.Model):
    comments = models.TextField(null=True)


# Модель отзывов
class Review(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(choices=RATING)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='reviews',
        blank=False,
        null=False
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # Реализуем ависимость Один-к-одному с моделью Comments
    comments = models.OneToOneField(
        Comments,
        on_delete=models.SET_NULL,
        null=True,
        related_name='review'
    )
