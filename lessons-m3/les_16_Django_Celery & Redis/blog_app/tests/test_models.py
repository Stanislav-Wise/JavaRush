import pytest
from blog_app.models import Author, Post


@pytest.mark.django_db
def test_create_author(author_1, author_2):
    assert Author.objects.count() == 2
    assert author_1.name == 'Боб'
    assert author_2.name == 'Мэри'
    assert str(author_1) == 'Боб!'


@pytest.mark.django_db
def test_create_post(post):
    """..."""
    assert Post.objects.count() == 1
    assert post.title == 'Тестовый пост'
    assert post.content == 'Содержание тестового поста'
    assert post.rating == 5
    assert post.author.name == 'Боб'
    assert str(post) == 'Тестовый пост!'