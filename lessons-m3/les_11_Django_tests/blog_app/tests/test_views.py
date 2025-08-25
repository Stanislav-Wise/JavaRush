import pytest
from django.urls import reverse
from blog_app.models import Post, Author


def test_home_view(client):
    """Тесты для проверки главной страницы."""
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert "Добро пожаловать" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_post_list_view(client, author_1, author_2, post, post_2):
    url = reverse('post_list')
    response = client.get(url)

    assert response.status_code == 200
    # assert post in response.content.decode("utf-8")
    assert post.title.encode() in response.content
    assert author_1.name.encode() in response.content