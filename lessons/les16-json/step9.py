import json


with open("employees.json", "r", encoding="utf-8") as f:
    load_employees =json.load(f)

print(load_employees)
print(type(load_employees))