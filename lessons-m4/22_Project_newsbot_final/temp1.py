data =  {"name": "Bob", "age": 20}
print(data.get('name')) # Выведет Bob
print(data.get('city')) # Выведет None
print(data.get('city', 'Москва')) # Выведет Москва

print(data['city']) # Выведет Bob