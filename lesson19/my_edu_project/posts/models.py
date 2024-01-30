from django.db import models
from django.contrib.auth import get_user_model


RATING = [(1, 'Плохо'), (2, 'Посредственно'), (3, 'Нормально'), (4, 'Хорошо')]


User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=15, unique=True, null=False)


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        help_text='Заголовок',
        # Читабельное имя поля, влияет на отображение поля в админке
        # и элемент label.
        verbose_name='Заголовок публикации'
    )
    text = models.TextField(
        blank=False,
        help_text='Текст',
        verbose_name='Текст публикации'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        help_text='Автор',
        verbose_name='Автор'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='posts',
        through='PostTag',
        help_text='Теги',
        verbose_name='Теги публикации'
    )

    class Meta:
        ordering = ['-pub_date']
        # Читабельное имя модели, отображается в админке
        verbose_name = 'Публикация'
        # Читабельное имя во множественном числе, отображается в админке
        verbose_name_plural = 'Публикации'

    # Способ задания имени отдельной записи в админке
    def __str__(self):
        return f'{self.title[:30]} -- {self.pub_date}'


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Comments(models.Model):
    comments = models.TextField(null=True)


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
    comments = models.OneToOneField(
        Comments,
        on_delete=models.SET_NULL,
        null=True,
        related_name='review'
    )
