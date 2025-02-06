import json


data = {
    "users": [
        {1: "Боб", "active": True},
        {"username": "jane_smith", "active": False}
    ]
}

print(type(data))

with open("users.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)