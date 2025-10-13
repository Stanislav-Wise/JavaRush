from django.core.management.base import BaseCommand
from blog_app.models import Post, Comment, Author, Tag, AuthorProfile
from random import randint, choice



class Command(BaseCommand):
    help = 'Генерация данных нашей модели'

    def handle(self, *args, **kwargs):
        """Выполняет создание тестовых данных."""
        self.stdout.write('Начинается генерация...')

        # result = random.randint(1, 10)
        author_list = []
        self.stdout.write('Начинается генераци авторов...')
        for i in range(5):
            author_name = f'Автор {i + 1}'
            author = Author.objects.create(name=author_name)
            author_list.append(author)
        self.stdout.write(f'Генерация авторов завершена')

        tag_list = []
        self.stdout.write('Начинается генераци тэгов...')
        for i in range(5):
            tag_name = f'Tag{i + 1}'
            tag = Tag.objects.create(name=tag_name)
            tag_list.append(tag)
        self.stdout.write(f'Генерация тэгов завершена')

        post_list = []
        self.stdout.write('Начинается генераци постов...')
        for i in range(7):
            post_title = f'Пост {i + 1}'
            post_content = f'Контент Поста {i + 1}'
            post_author = choice(author_list)
            post = Post.objects.create(title=post_title, content=post_content, author=post_author)
            post_list.append(post)

        self.stdout.write(f'Генерация постов завершена')

        comment_list = []
        self.stdout.write('Начинается генераци коментов...')
        for i in range(7):
            comment_post = choice(post_list)
            comment_author = choice(author_list)
            comment_text = f'Комент к Посту {comment_post} от автора {comment_author}'
            comment = Comment.objects.create(post=comment_post, author=comment_author, text=comment_text)
            comment_list.append(comment)

        self.stdout.write(f'Генерация коментов завершенаю. Создано {len(comment_list)} коментов')

        self.stdout.write(f'Генерация данных завершена')