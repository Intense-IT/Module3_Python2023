from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Category(models.Model):
    """Модель категорий."""

    title = models.CharField('Название категории', max_length=150, blank=False)

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title[:20]


class Tag(models.Model):
    """Модель тегов."""

    name = models.SlugField('Имя тега', max_length=15, null=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    """Модель публикаций."""

    title = models.CharField('Заголовок публикации', max_length=155,
                             blank=False)
    text = models.TextField('Текст публикации', blank=False)
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)
    update_date = models.DateTimeField('Дата изменения', auto_now=True)
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Автор публикации'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Категория публикации'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='posts',
        through='PostTag',
        verbose_name='Теги публикации'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self) -> str:
        return self.title[:20]


class PostTag(models.Model):
    """Промежуточная модель для отношения ManyToMany моделей Post и Tag."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['post', 'tag'], name='post_tag')]
