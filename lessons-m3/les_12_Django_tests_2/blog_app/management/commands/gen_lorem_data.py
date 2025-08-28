from django.core.management.base import BaseCommand
from blog_app.models import Post, Comment, Author, Tag, AuthorProfile
from random import randint, choice
from faker import Faker



class Command(BaseCommand):
    help = 'Генерация данных нашей модели'

    def handle(self, *args, **kwargs):
        """Выполняет создание тестовых данных."""
        self.stdout.write('Начинается генерация...')

        fake = Faker()

        author_numbers = randint(3, 5)
        author_list = []
        self.stdout.write('Начинается генераци авторов...')
        for i in range(author_numbers):
            author_name = fake.name()
            author = Author.objects.create(name=author_name)
            author_list.append(author)
        self.stdout.write(f'Генерация авторов завершена')

        tag_list = []
        self.stdout.write('Начинается генераци тэгов...')
        for i in range(5):
            tag_name = fake.word()
            tag = Tag.objects.create(name=tag_name)
            tag_list.append(tag)
        self.stdout.write(f'Генерация тэгов завершена')

        post_numbers = randint(7, 10)
        post_list = []
        self.stdout.write('Начинается генераци постов...')
        for i in range(post_numbers):
            post_title = fake.sentence(nb_words=5)
            post_content = fake.text(max_nb_chars=200)
            post_author = choice(author_list)
            post = Post.objects.create(title=post_title, content=post_content, author=post_author)
            post_list.append(post)

        self.stdout.write(f'Генерация постов завершена')

        comment_list = []
        self.stdout.write('Начинается генераци коментов...')
        comment_numbers = randint(7, 15)
        for i in range(comment_numbers):
            comment_post = choice(post_list)
            comment_author = choice(author_list)
            comment_text = fake.text(max_nb_chars=100)
            comment = Comment.objects.create(post=comment_post, author=comment_author, text=comment_text)
            comment_list.append(comment)

        self.stdout.write(f'Генерация коментов завершенаю. Создано {len(comment_list)} коментов')

        self.stdout.write(f'Генерация данных завершена')