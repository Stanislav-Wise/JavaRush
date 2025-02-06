import http.client
from http.client import responses

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

print(type(conn))

conn.request("GET", "/posts/1")

response = conn.getresponse()

print(response.status)

res_data = response.read().decode("utf-8")
print(res_data)

conn.close()