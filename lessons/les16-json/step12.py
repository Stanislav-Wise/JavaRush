import requests


url = "https://jsonplaceholder.typicode.com/posts/"

data = {
    "title": True,
    1: "bar",
    "userId": 1
}

response = requests.post(url, json=data)
print(response.status_code)

if response:

    print(response.json())
# print(response.text)