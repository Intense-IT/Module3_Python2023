# Модели
from django.db import models
from django.contrib.auth import get_user_model


RATING = [(1, 'Плохо'), (2, 'Посредственно'), (3, 'Нормально'), (4, 'Хорошо')]


# Модель пользователя встроена в Django и импортируется следующим образом:
User = get_user_model()


# Модель публикаций
class Post(models.Model):
    # Поля модели
    # Возможные типы полей - IntegerField, FloatField, EmailField, FileField,
    # ImageField, BooleanField, и т.д.

    # Возможные аргументы полей:
    # - max_length (максимальное длина значения поля),
    # - unique (значение записи в таблице уникально),
    # - blank (разрешено пустое поле при заполнении формы),
    # - null (разрешено хранение пустого значения NULL),
    # - default (полю задается значение по умолчанию),
    # - auto_now_add (задаются текущие дата и время при добавлении записи),
    # - auto_now (задаются текущие дата и время при каждом изменении записи),
    # - choices (задается в виде списка определенный набор вариантов для поля),
    title = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False
    )
    text = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    # Внешний ключ для реализации отношения один-ко-многим.
    # Аргумент related_name задает имя, по которому можно получить
    # у определенного объекта все зависимые объекты данной модели.
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    # Класс Meta задает доп. установки данной модели.
    class Meta:
        # ordering - переопределяет поле сортировки записей в модели.
        # Знак "-" перед именем поля изменяет сортировку на убывающую.
        ordering = ['-pub_date']


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
    comments = models.TextField(blank=True, null=True, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
