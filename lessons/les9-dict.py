# my_dict = {}
# print(my_dict)
# print(type(my_dict))
#
#
# friends = {
#     'Bob': 25,
#     'Bob': 15,
#     'Rolf': 32,
#     'Anne': 21,
#     'John': 40,
# }
# print(friends)
#
#
# my_dict = dict()
# print(my_dict)
# print(type(my_dict))
#
#
# friends_data = [('Bob', 15), ('Anne', 21), ('John', ['qaz', 'asda']), ]
# friends_1 = dict(friends_data)
# print(friends_1)
#
#
# friends_2 = dict(Alice=25, Bob=17, John=23)
# print(friends_2)
#
#
# list_friends = ['Bob', 'Anne', 'John']
# friends_3 = dict.fromkeys(list_friends, 17)
# print(friends_3)
#
# friends_4 = {
#     'Bob': [{1, 2, 3,}, {4, 5, 6,}],
#     1: 15,
#     (1, 2): 32,
# }
# print(friends_4)

# friends = {}

# friends = {
#     'Bob': 15,
#     'Rolf': 32,
#     'Anne': 21,
#     'John': 40,
# }
# print(friends)
# print(len(friends))
# print(friends['Rolf'])
# print(friends.get('Bob123123'))
#
#
# print(friends.keys())
#
# for key in friends.keys():
#     print(f'Ключ {key}')
#
# print(friends.values())
#
# for value in friends.values():
#     print(f'Значение {value}')
#
# print(friends.items())
# for key, value in friends.items():
#     print(f'Ключ {key} Значение {value}')


# friends = {
#     'Bob': 15,
#     'Rolf': 32,
#     'Anne': 21,
#     'John': 40,
# }
# print(friends)

# keys = friends.keys()
# print(keys)
#
# friends['Mia'] = 29
# if 'Bob' not in friends:
#     friends['Bob'] = 17
# print(friends)
# # print(keys)
#
# print('Alice' in friends)
# print('Alice' in friends.keys())

# age = friends.setdefault('Bob', None)
# print(friends)
#
# friends['Bob'] = 19
# print(friends)
#
# friends.update({'John': 45, 'Mia': 10,})
# print(friends)

# del friends['Bob']
# print(friends)
#
#
# age = friends.pop('John1', "Ключа нет")
# print(friends)
# print(age)
#
#
# last_item = friends.popitem()
# print(friends)
# print(last_item)
#
# friends.clear()
# print(friends)



# friends = {
#     'Bob': 15,
#     'Rolf': 32,
#     'Anne': 21,
#     'John': 40,
# }
# print(friends)

# for index, (key, value) in enumerate(friends.items()):
#     print(index, key, value)

# items = friends.items()
# print(items)

# nums = {x: x**2 for x in range(1, 6) if x % 2 == 0}
# print(nums)
#
# friends_list = [
#     'Bob',
#     'Rolf',
#     'Anne',
#     'John',
# ]
#
# name_leng = {name: len(name) for name in friends_list if not name.startswith('B')}
# print(name_leng)




# friends_data = [['Bob', 15], ['Anne', 21], ['John', 17]]
#
# friends_new = {name: age for name, age in friends_data}
# print(friends_new)

friends = {
    'Bob': {'age': 17, 'city': "Moscow" },
    'Bob1': {'age': 18, 'city': "Moscow1" },
    'Bob2': {'age': 19, 'city': "Moscow2" },

}
# print(friends.get("details").get('city'))
# print(friends["details"]['city'])
for name, det in friends.items():
    print(name, det)
    print(friends.get('city'))
    # for key, value in det.items():
    #     print(key, value)