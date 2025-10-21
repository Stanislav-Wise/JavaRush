import requests


# url = 'http://127.0.0.1:8000/api/v1/token/'
# # http://127.0.0.1:8000/api/v1/token/refresh/
# payload = {'email': 'admin@mail.com', 'password': '1'}
# response = requests.post(url, json=payload)
# print(response.status_code)
# print(response.json())

# payload = {'email': 'admin@mail.com', 'password': '1'}
# response = requests.post(url, headers=headers, json=data)


# curl -X POST "http://127.0.0.1:8000/api/v1/authors/" -H "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYwOTc4MjA5LCJpYXQiOjE3NjA5Nzc5MDksImp0aSI6ImYxMzhhOWRlN2RhYjQwOTE5ZWI4MzBkYmQ4ODdkMThjIiwidXNlcl9pZCI6IjEifQ.7Xgd5bjAqKtS7w--aPJNA7oPQO_aWprmYk85g2yGnro" -H "Content-Type: application/json" -d '{"name": "Tanos1"}'


# url = 'http://127.0.0.1:8000/api/v1/authors/'
# ACCESS = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYwOTc4NTc2LCJpYXQiOjE3NjA5NzgyNzYsImp0aSI6ImVkYzc4YWYwMzk2MTRlYjg5MmQwYTk2N2RhMDIyMmI3IiwidXNlcl9pZCI6IjEifQ.xbFuSQySq8AJ8zEqwsKu6C939hEud3Jz61RTUYd5meI"
# headers = {
# "Authorization": f"Bearer {ACCESS}",
# "Content-Type": "application/json",
# }
#
# data = {
#     "name": "Tanos5",
# }
#
# response = requests.get(url, headers=headers)
# print(response.status_code)
# # print(response.json())



refresh_url = 'http://127.0.0.1:8000/api/v1/token/refresh/'
refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2MTA2NDY3NiwiaWF0IjoxNzYwOTc4Mjc2LCJqdGkiOiI4ZmYxNGU3MDdlNDE0YzdiYjJlMzBmZWQwMWYxNDAzZiIsInVzZXJfaWQiOiIxIn0.AgicCNmzq2dDIIU6W0arcExI_8kS2f7-aDTIzNMIQK4"
new_access = ''
refresh_data = {"refresh": refresh_token}
refresh_response = requests.post(refresh_url, json=refresh_data)
print(f"Refresh Status: {refresh_response.status_code}")
print(f"New Tokens: {refresh_response.json()}")

if refresh_response.status_code == 200:
    new_access = refresh_response.json()['access']
    print(f"New Access Token: {new_access}")


url = 'http://127.0.0.1:8000/api/v1/authors/'
ACCESS = new_access
headers = {
"Authorization": f"Bearer {ACCESS}",
"Content-Type": "application/json",
}

data = {
    "name": "Tanos5",
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
# # print(response.json())
