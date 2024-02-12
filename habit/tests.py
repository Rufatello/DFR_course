from django.contrib.auth import login
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
    def setUp(self):

        """К сожалению с присвоением Юзера не заработало, полагаю что это в связи с верификацией, потому что по дефолту стоит Is_active = False"""
        # self.user = User.objects.create(email='1@mail.ru',  password='12345')
        # self.user.set_password('12345')
        # self.user.save()
        # login_successful = self.client.login(username='1@mail.ru', password='12345')
        # self.assertTrue(login_successful)
        self.habit = Habit.objects.create(action='asdasd')

    def test_reflex_create(self):
        # response = self.client.post('/api/token/', {"email": "1@mail.ru", "password": "12345"})
        # self.access_token = response.json().get("access")
        # self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        # print(response.json())
        habit = Habit.objects.create(action='asdasd')
        data = {
            # 'user': self.user.pk,
            'locale': '123',
            'data': '2021-01-01',
            'is_publicity': False,
            'periodicity': 'week',
            'nice_reflex': False,
            'action': '321',
            'time_to_complete': 12,
            'habit': self.habit.pk
        }
        response = self.client.post('/habit/reflex/create/', data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # session_data = self.client.session
        # print(session_data)

    def test_delete(self):
        data = {
            'locale': '123',
            'data': '2021-01-01',
            'is_publicity': False,
            'periodicity': 'week',
            'nice_reflex': True,
            'action': '321',
            'time_to_complete': 12,
            'fee': 123
        }
        response = self.client.delete('/habit/reflex/2/delete/', data=data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print(response.json())


