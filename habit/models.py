from django.db import models
from config import settings
from users.models import NULLABLE


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    action = models.CharField(verbose_name='Действие', max_length=150)

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'


class Reflex(models.Model):
    periodicity = [
        ('week', 'Раз в неделю'),
        ('every_day', 'Каждый день')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    locale = models.CharField(max_length=100, verbose_name='Место действия')
    data = models.DateTimeField(verbose_name='Время действия')
    periodicity = models.CharField(choices=periodicity, default='every_day', verbose_name='Переодичность')
    nice_reflex = models.BooleanField(default=False, verbose_name='признак привычки')
    is_publicity = models.BooleanField(verbose_name='признак публикации')
    fee = models.CharField(verbose_name='Вознагрождение', max_length=150, **NULLABLE)
    action = models.CharField(verbose_name='Действие', max_length=150)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, verbose_name='Привычка', **NULLABLE)
    time_to_complete = models.PositiveIntegerField(verbose_name='Время на выполение')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Рефлекс'
        verbose_name_plural = 'Рефлексы'





