# Своя модель пользователя
from django.db import models
# При создания своей модели пользователя необходимо воспользоваться
# встроенным классом, AbstractUser или AbstractBaseUser.
# Оба они импортируются из модели django.contrib.auth.models.
from django.contrib.auth.models import AbstractUser


# AbstractUser и AbstractBaseUser
# Отличия классов заключаются в том, что в случае наследования от AbstractUser
# мы добавляем свои поля к уже имеющися в модели User.
# При наследовании от AbstractBaseUser поля модели User не передаются,
# только система аутентификации встроенная в Django.
class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True)
    is_married = models.BooleanField(null=True)
