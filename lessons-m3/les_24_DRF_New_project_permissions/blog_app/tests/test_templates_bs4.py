import pytest
from bs4 import BeautifulSoup
from django.urls import reverse


# @pytest.mark.django_db
# def test_post_list_template(client, author_1, author_2, post, post_2):
#     url = reverse('post_list')
#     response = client.get(url)
#
#     assert response.status_code == 200
#
#     soup = BeautifulSoup(response.content, 'html.parser')
#     # titles = [h5.get_text() for h5 in soup.find_all('h5')]
#     # assert 'Тестовый пост' in titles
#     # assert 'Тестовый пост 2' in titles
#
#     # assert soup.find(string='Автор: Боб | Рейтинг: 5')
#     # assert 'Боб' in soup.get_text()
#     assert soup.find('small', text='Автор: Боб | Рейтинг: 5')


@pytest.mark.django_db
def test_post_detail_template(client, author_1, author_2, post, post_2):
    url = reverse('post_detail', args=[post.id])
    response = client.get(url)

    assert response.status_code == 200

    soup = BeautifulSoup(response.content, 'html.parser')

    # assert soup.find('h1', text='Тестовый пост')
    # assert soup.find('p', text='Содержание тестового поста')
    # assert soup.find('i', text=' Рейтинг: 5 ')

