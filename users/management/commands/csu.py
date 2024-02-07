from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='1@mail.ru',
            first_name='Rufat',
            last_name='Geydarov',
            surname='Gasrat ogly',
            is_staff=True,
            is_active=True,
            is_superuser=True
        )
        user.set_password('12345')
        user.save()