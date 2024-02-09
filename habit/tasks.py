from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta
import pytz
import requests
from habit.models import Reflex
from celery import shared_task
import telebot
from celery import shared_task
from telebot import TeleBot
from django.conf import settings

@shared_task
def message():
    timezone.activate('Europe/Moscow')
    today = datetime.now()
    moskow_tz = pytz.timezone('Europe/Moscow')
    today = today.astimezone(moskow_tz)
    print(today)

    a = Reflex.objects.all()
    for reflex in a:
        print(reflex.data)
        if reflex.periodicity == 'every_day' and reflex.data <= today:
            params = {'chat_id': 1473590803,
                      "text": f"Эй ты{reflex.user.last_name}, пришло время для {reflex.action},"
                      }
            requests.get(f'https://api.telegram.org/bot{reflex.user.token}/sendMessage', params=params).json()
            reflex.data= datetime.now().astimezone(moskow_tz) + timedelta(days=1)
            reflex.save()
        elif reflex.periodicity == 'week' and reflex.data <= today:
            params = {'chat_id': 1473590803,
                      "text": f"Эй ты{reflex.user.last_name}, пришло время для {reflex.action}"
                      }
            requests.get(f'https://api.telegram.org/bot{settings.MY_TOKEN}/sendMessage', params=params).json()
            reflex.data= datetime.now().astimezone(moskow_tz) + timedelta(days=7)
            reflex.save()

