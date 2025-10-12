import requests


url = 'http://127.0.0.1:8000/api/v1/token/'
# http://127.0.0.1:8000/api/v1/token/refresh/
payload = {'email': 'admin@mail.com', 'password': '1'}
response = request.post(url, json=payload)
print(response.status_code)
print(response.json())
