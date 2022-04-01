from django.core.management.base import BaseCommand
from authapp.models import LibUser
from uuid import uuid4


class Command(BaseCommand):
    def handle(self, *args, **options):
        super_user = LibUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
        user1 = LibUser.objects.create_user('Alice', 'alice@geek.ru', 'geekbrains')
        user2 = LibUser.objects.create_user('Mary', 'mary@geek.ru', 'geekbrains')
