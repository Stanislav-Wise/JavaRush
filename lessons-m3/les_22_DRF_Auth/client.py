import requests


BASE_URL = 'http://localhost:8000'
TOKEN_URL = f'{BASE_URL}/api/v1/token/'
REFRESH_URL = f'{TOKEN_URL}refresh/'
HABITS_URL = f'{BASE_URL}/api/v1/habits/'


creds = {
    "username": "bob",
    "password": "1@3$5qWeRt"
}

response = requests.get(HABITS_URL)
# response = requests.post(TOKEN_URL, json=creds)
# response = requests.get(HABITS_URL)
print(response.status_code)
print(response.content)