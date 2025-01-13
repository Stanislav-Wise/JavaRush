# name = 'Bob'
#
# students = (name, 'Вася', 'Вася', 'Петя', 'Маша', 'Даша', 'Катя', True, 123, 1.2, [1, 2, 3])
# print(students)
# print(type(students))
#
# names = tuple(['Петя', 'Маша', 'Даша', 'Катя'])
# print(names)
# print(type(names))
#
# name_tuple = ('Варя', )
# print(name_tuple)
# print(type(name_tuple))
#
# my_tuple = 1, 2, 3, 4
# print(my_tuple)
# print(type(my_tuple))
#
# my_tuple_1 = 1,
# print(my_tuple_1)
# print(type(my_tuple_1))

# names_list = list(names)
# print(names_list)
# print(type(names_list))


# names = tuple(['Петя', 'Маша', 'Даша', 'Катя',  'Вася', 'Вася', 'Петя', 'Маша', 'Даша', 'Катя'])
# print(names)
# print(type(names))
#
# print(names[::-1])
#
# if 'Петя1111' not in names:
#     print('Yes')
# else:
#     print('No')
#
# print(len(names))

# names_age = (('Игорь', 35, 2, 3, 4, 5, 1), ('Боб', 25), ('Анна', 17), ('Гоша', 91), ('Маша', 34))
# print(names_age)
# print(type(names_age))
# print(len(names_age))
#
# new_names = ('Игорь', 35, 2, 3, 4, 5, 1)
# print(names_age[0][0])
# name,  my_bool, num_1,  *_ = names_age[0]
#
# name,  *_, my_bool, num_1  = new_names # ('Игорь', 35, 2, 3, 4, 5, 1)
#
# print(name)
# print(_)
# print(my_bool)


# names_age = (('Игорь', 35, ('Боб', 25)), ('Боб', 25), ('Анна', 17), ('Гоша', 91), ('Маша', 34))
# print(names_age[0][2][0])
# names_age_list = list(names_age)
# print(names_age_list)
# print(type(names_age_list))
# n = names_age_list.pop(0)
# print(n)
# print(names_age_list)
#
# names_age_new = tuple(names_age_list)
# print(names_age_new)
#
#
# for n, a in names_age_new:
#     print(n, a)

# numbers = (5, 2, 7, 3, 8)
# print(numbers)
# num_new = tuple(sorted(numbers))
# print(num_new)
# print(id(num_new))
#
# # all_num = num_new + numbers
# num_new = numbers * 5
#
# # all_num = tuple([*num_new, *numbers])
#
#
# print(num_new)
# print(type(num_new))
# print(id(num_new))

# original_tuple = (1, 2, 3, 4, 5)
# print(original_tuple)
# print(id(original_tuple))
# # Копирование кортежа с помощью прямого присваивания
# copied_tuple = tuple(original_tuple)
# print(copied_tuple)
# print(id(copied_tuple))
#
# a = 1000000000000000000000000
# print(a)
# print(id(a))
# b = 1000000000000000000000000
# print(b)
# print(id(b))

#
# from itertools import chain
#
# # Определение исходных кортежей
# tuple1 = (1, 2, 1)
# tuple2 = (4, 5, 6)
# tuple3 = (7, 1, 9)
# # Объединение кортежей с помощью chain
# combined_tuple = tuple(chain(tuple1, tuple2, tuple3))
# print(combined_tuple) # Вывод: (1, 2, 3, 4, 5, 6, 7, 8, 9)
#
# print(combined_tuple.count(1))
# print(combined_tuple.index(1))
# print(sum(combined_tuple))
# print(max(combined_tuple))
# print(min(combined_tuple))

#
# Дополните приведенный код так, чтобы переменная new_tuples содержала список кортежей на основе списка tuples с последним элементом каждого кортежа, замененным на численное значение 100
tuples = [(10, 20, 40), 1, 2, (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]

# new_tuples = [t[:-1] + (100,) for t in tuples]
# print(new_tuples)


for t in tuples:
    print(t)