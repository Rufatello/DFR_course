from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=70, verbose_name='Имя')
    last_name = models.CharField(max_length=70, verbose_name='Фамилия')
    surname = models.CharField(max_length=70, verbose_name='Отчество')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    code = models.CharField(max_length=15, verbose_name='код', **NULLABLE)
    token = models.CharField(default=settings.MY_TOKEN, verbose_name='Токен телеграмма')

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'