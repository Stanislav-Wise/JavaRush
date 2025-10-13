import pytest
from blog_app.models import Post, Author


@pytest.fixture
def author_1():
    return Author.objects.create(name='Боб')


@pytest.fixture
def author_2():
    return Author.objects.create(name='Мэри')


@pytest.fixture
def post(author_1):
    return Post.objects.create(
        title='Тестовый пост',
        content="Содержание тестового поста",
        rating=5,
        author=author_1

    )


@pytest.fixture
def post_2(author_2):
    return Post.objects.create(
        title='Тестовый пост 2',
        content="Содержание тестового поста 2",
        rating=7,
        author=author_2

    )