import json


with open("users.json", "r", encoding="utf-8") as f:
    load_users =json.load(f)

print(load_users)
print(type(load_users))