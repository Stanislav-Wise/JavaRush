import json


data = {
    "name": "Алиса",
    "age": 28,
    "languages": ["Python", "JavaScript"],
    "is_student": False
}

json_str = json.dumps(data, ensure_ascii=False)
print(json_str)
print(type(json_str))

pars_json = json.loads(json_str)
print(pars_json)
print(type(pars_json))