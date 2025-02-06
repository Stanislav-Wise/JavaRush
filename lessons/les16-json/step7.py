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

# json_str = json.dumps(employees, ensure_ascii=False)
# print(json_str)
# print(type(json_str))


my_str ="""{"department": "Research & Development", "employeeCount": 3, "isRemoteTeam": false, "members": [{"name": "Alice", "age": 29}, {"name": "Bob", "age": 34}, {"name": "Eve", "age": 25}]}"""
pars_json = json.loads(my_str)
print(pars_json)
print(type(pars_json))