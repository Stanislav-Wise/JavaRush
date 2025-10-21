import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_post_list_template(client, author_1, author_2, post, post_2):
    url = reverse('post_list')
    response = client.get(url)

    assert response.status_code == 200

    assert 'Тестовый пост' in response.content.decode('utf-8')
    assert 'Тестовый пост 2' in response.content.decode('utf-8')
    assert 'Автор: Боб' in response.content.decode('utf-8')
    assert 'Автор: Мэри' in response.content.decode('utf-8')


@pytest.mark.django_db
def test_post_detail_template(client, author_1, author_2, post, post_2):
    url = reverse('post_detail', args=[post.id])
    response = client.get(url)

    assert response.status_code == 200

    assert 'Детальный пост!' in response.content.decode('utf-8')
    assert 'Рейтинг: ' in response.content.decode('utf-8')
    assert 'Дата создания: ' in response.content.decode('utf-8')

    assert '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"' in response.content.decode('utf-8')
