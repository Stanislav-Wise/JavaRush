import requests

url = "https://jsonplaceholder.typicode.com/posts"
url_2 = "https://mail.ru"

response = requests.get(url)
response_2 = requests.get(url_2)

print(response.status_code)
print(response_2.status_code)

print(response.json())
# print(response_2.text)