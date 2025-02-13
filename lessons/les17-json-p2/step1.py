import requests


api_key = "eeeee"
api_url = "https://api.openweathermap.org/data/2.5/weather"
# api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&APPID={api_key}"

city = "Moscow"
params = {"q": city, "units": "metric", "lang": "ru", "APPID": api_key}
response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()
    print(f'Погода в городе {city}: {data["weather"][0]["main"]}, {data["weather"][0]["description"]}')
    print(data['main']['temp'])
else:
    print(f'Произошла ошибка: {response.status_code}')
