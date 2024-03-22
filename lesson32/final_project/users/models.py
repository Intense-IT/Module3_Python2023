from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Кастомная модель пользователя."""

    USER = 'u'
    MODERATOR = 'm'
    ADMINISTRATOR = 'a'
    ROLE_CHOICES = [
        (USER, 'User'),
        (MODERATOR, 'Moderator'),
        (ADMINISTRATOR, 'Administrator')
    ]
    role = models.CharField(
        'Роль пользователя',
        max_length=1,
        choices=ROLE_CHOICES,
        default=USER
    )

    def __str__(self) -> str:
        return self.username
