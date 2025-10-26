import requests
from pprint import pprint


base_url = 'http://127.0.0.1:8000/api/v1'
USER = 'admin@mail.com'
PASSWORD = '1'

# token
token_url = f'{base_url}/token/'
user_payload = {
    'email': USER,
    'password': PASSWORD,
}

response = requests.post(token_url, json=user_payload)

print(response.status_code)
if response.status_code:
    access_token = response.json().get('access')
    refresh_token = response.json().get('refresh')
    print(access_token)
    print(refresh_token)


# GET запрос /posts/
print('ИЗНАЧАЛЬНЫЙ СПИСОК ПОСТОВ')
posts_url = f'{base_url}/posts/'
response = requests.get(posts_url)
print(response.status_code)
if response.status_code:
    pprint(response.json())


# POST запрос /posts/
print('ДОБАВЛЕНИЕ ПОСТА')
headers = {
    'Authorization': f'Bearer {access_token}',
}

post_payload = {
    'title': 'Новый API пост',
    'content': 'Контент для Нового API поста',
    'rating': 1,
    'tags': [],
    'author': 4,
}
posts_url = f'{base_url}/posts/'
response = requests.post(posts_url, headers=headers, json=post_payload)
print(response.status_code)
if response.status_code:
    pprint(response.json())


# GET запрос /posts/
print('НОВЫЙ СПИСОК ПОСТОВ')
posts_url = f'{base_url}/posts/'
response = requests.get(posts_url)
print(response.status_code)
if response.status_code:
    pprint(response.json())


# GET запрос /posts/1/
print(' ПОСТ')
posts_url = f'{base_url}/posts/1/'
response = requests.get(posts_url)
print(response.status_code)
if response.status_code:
    print(response.json())


# GET запрос /authors/4/
print('АВТОР')
posts_url = f'{base_url}/authors/4/'
response = requests.get(posts_url)
print(response.status_code)
if response.status_code:
    print(response.json())


# DELETE запрос /posts/13/
print('УДАЛЯЕМ ПОСТ')
posts_url = f'{base_url}/posts/13/'
response = requests.delete(posts_url, headers=headers)
print(response.status_code)
if response.status_code:
    print('Удалили пост')

# requests.delete
# requests.put