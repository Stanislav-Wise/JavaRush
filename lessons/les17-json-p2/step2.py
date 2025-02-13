import requests


api_key = "ccccc"

movie_title = "Tom and Jerry"

api_url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    print(f'Название фильма: {data["Title"]}')
    print('Рейтинг: ', data["imdbRating"])
    print('Режиссер: ', data["Director"])
    print('Продолжительность: ', data["Runtime"])
    print('Год выпуска: ', data["Year"])
    print('Страна: ', data["Country"])
    print('Сюжет: ', data["Plot"])
else:
    print(f'Произошла ошибка: {response.status_code}')

