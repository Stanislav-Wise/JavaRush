import json


employees = {
    "department": "Research & Development",
    "employeeCount": 3,
    "isRemoteTeam": False,
    "members": [
        {"name": "Alice", "age": 29},
        {"name": "Bob",   "age": 34},
        {"name": "Eve",   "age": 25}
    ]
}


with open("employees.json", "w", encoding="utf-8") as f:
    json.dump(employees, f, indent=2)

# print(type(employees))