import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(response.status_code)
user = response.json()

head = response.headers
print(head['Content-Type'])
print(user['title'])

print(type(response))