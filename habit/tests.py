from rest_framework import status
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from habit.models import Habit
from users.models import User

class HabitTestCase(TestCase):

    def setUp(self):
        self.habit = Habit.objects.create(
            action='asdasd',
        )

    def test_habit_create(self):
        """Создание привычки"""

        data = {
            'action': '3123'
        }
        response = self.client.post(
            '/habit/habit/',
            data=data
        )
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_habit_list(self):
        """Test List"""

        response = self.client.get(
            '/habit/habit/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)

        self.assertEquals(
            response.json(),
            [{'id': 5, 'action': 'asdasd', 'user': None}]

        )

    def test_habit_delete(self):
        data = {'id': 1, 'action': 'asdasd'}
        response = self.client.post(
            '/habit/habit/',
            data=data

        )
        response = self.client.get(
            '/habit/habit/1/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(
            '/habit/habit/1/',

        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update(self):
        data = {'id': 1, 'action': 'asdasd'}
        """обновление урока"""

        response = self.client.get(
            '/habit/habit/1/',
            data=data
        )
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.put(
            '/habit/habit/1/',
            data=data

        )
        print(response.json())
        self.assertEquals(response.json(),
                          {'id': 1, 'action': 'asdasd', 'user': None}
                          )


class ReflexTestCase(TestCase):
    def test_reflex_create(self):
        data = {
            'locale': '123',
            'data': '01-01-2021',
            'is_publicity': False,
            'periodicity': 'week',
            'nice_reflex': False,
            'action': '321',
            'time_to_complete': 12,
        }
        responce = self.client.post(
            '/habit/reflex/create/',
            data=data
        )
        print(responce)
        self.assertEqual(
            responce.status_code, status.HTTP_201_CREATED
        )

