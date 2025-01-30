# name_1 = 'Bob'
# name_2 = 'Ann'
# name_3 = 'Tom'
# name_4 = 'Alice'
# name_5 = 'Kate'
#
# names = [
#     name_1,
#     name_2,
#     name_3,
#     name_4,
#     name_5
# ]
#
# name_new = ['Bob', max(2, 3)]
#
# print(names)
# print(name_new)
#
# print(type(names))
# print(type(name_new))

# new_list = []
# new_list_1 = list()
#
# print(new_list)
# print(new_list_1)
#
# print(type(new_list))
# print(type(new_list_1))
# my_str = 'Python'
#
# for ch in my_str:
#     print(ch)

# my_list = [1, 2, 3, 4, 5, 'string', True, [1, 2, 3]]
# print(my_list)
#
# num = len(my_list)
# print(num)
#
# print(my_list[0])
# print(my_list[3])
# print(my_list[num - 1])
#
# print(my_list[-2])


# if type(my_list) == list:
#     print('Это список')


# my_list = []
# print(my_list)
# my_list.append(123)
# print(my_list)


name_1 = 'Bob'
name_2 = 'Ann'
name_3 = 'Tom'
name_4 = 'Alice'
name_5 = 'Kate'
names = [name_1, name_2, name_3, name_4, name_5]
print(names)

names.append('John')
print(names)

names.insert(2, 'Max')
print(names)

list_names = ['Ivan', 'Petr', 'Bob', 'Sidor']
names.extend(list_names)
# names = names + list_names
print(names)

names.remove('Bob')
print(names)

name_removed = names.pop()
print(names)
print(name_removed)

name_removed = names.pop(1)
print(names)
print(name_removed)

# names.clear()
# print(names)

# del names[1]
# print(names)
#
# names_1 = names[:5]
# print(names_1)
# print(names)
#
# name = 'Bob'
# if name in names:
#     print('Yes')
# else:
#     print('No')
#
# for i in range(len(names)):
#     if names[i] == name:
#         print('Yes')
#     else:
#         print('No')

print(names)
# for name1 in names:
#     name1 = 123

print(names)

# for i, name in enumerate(names[3::2]):
#     names[i] = 123
#
# print(names)

# inx = 0
# while inx < len(names):
#     print(names[inx])
#     inx += 1

# print(names)
# my_list  = names[3:7]
# print(my_list)

# numbers = [str(x) for x in range(10) if x % 2 == 0]
# print(numbers)
#
# numbers_1 = []
# for x in range(10):
#
#     if x % 2 == 0:
#         numbers_1.append(x**2)
# print(numbers_1)
#
# long_name = [name for name in names if len(name) > 3]
# print(long_name)
#
#
# mult_table = [f'{i} * {j} = {i * j}' for i in range(1, 4) for j in range(1, 4)]
# print(mult_table)
#
# mult_table_1 = []
# for i in range(1, 4):
#     for j in range(1, 4):
#         mult_table_1.append(f'{i} * {j} = {i * j}')
# print(mult_table_1)

# my_numbers = [1, 5, 7, 3, 9, 2, 4, 6, 8, 0]
# print(my_numbers)
# # my_numbers.sort()
# # print(sorted(my_numbers))
#
# my_numbers.sort(reverse=True)
# print(my_numbers)

# names.sort(key=len, reverse=True)
# print(names)

print('*'*50)
new_names = names.copy()

print(names)
print(new_names)

names.pop()
print(names)
print(new_names)

import copy
new_names = copy.deepcopy(names)
print(names)
print(new_names)

names.pop()
print(names)
print(new_names)