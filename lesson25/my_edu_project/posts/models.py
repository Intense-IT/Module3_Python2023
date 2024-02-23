from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    # Вместо auto_now_add задаем значение даты по умолчанию через timezone.now,
    # работает схожим с datetime.now() образом, но с поправкой на часовой пояс.
    # Это дает нам возможность передавать свое или изменять значение даты в БД.
    pub_date = models.DateTimeField(default=timezone.now)
