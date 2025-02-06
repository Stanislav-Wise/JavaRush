import requests
from werkzeug.wsgi import responder

url = "https://ya.ru/search/"

params = {
    "text": "собака",
}

response = requests.get(url, params=params)
print(response.status_code)
print(response.text)