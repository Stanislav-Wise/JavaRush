from django.core.management.base import BaseCommand
from blog_app.models import Post, Comment, Author, Tag, AuthorProfile
import random


class Command(BaseCommand):
    help = 'Генерация данных нашей модели'

    def handle(self, *args, **kwargs):
        """Выполняет создание тестовых данных."""
        self.stdout.write('Начинается генерация...')

        result = random.randint(1, 100)

        self.stdout.write(f'Генерация данных завершена {result}')