my_dict = {
    'name': 'Bob',
    'age': 25,
    'my_print': print,
}

my_dict['my_print']('Hello !!!')

for item in my_dict:
    print(item)

print()
for item in my_dict.keys():
    print(item)

print()
for item in my_dict.values():
    print(item)

print()
for item in my_dict.items():
    print(item)