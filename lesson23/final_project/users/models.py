from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    '''Кастомная модель пользователя.'''
    birth_year = models.DateField(
        verbose_name='Год рождения',
        blank=False,
        null=True,
    )

    class Meta:
        ordering = ['birth_year']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username[:20]
