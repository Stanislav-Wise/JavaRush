# a = (2 + 2) * 2
# print(a)
#
# num_1 = 5
# print(num_1)
#
# # num_1 = num_1 - 10
# num_1 -= 10
#
# print(num_1)

# a = a <= b and b ==  c
#
# print(a)


# age = 25
# is_adult = age >= 18
# print(is_adult)

# number = 9
# is_even = number % 2 == 0
# print(is_even)

# print('Hello world')
# msg = 'Enter your name: '
#
# name = input(msg)
# print('Hello world', name)

# name = input("Введите ваше имя: ")
# print('Hello world' + name)
# print('Hello world', name)
# print(5 + 10 * 2)


# num = int(input("Введите число: "))

# num_user = input("Введите число: ")
# print(type(num_user))
# num = int(num_user)
# print(type(num))
# # num = '10'
# result = 5 * num
# print(type(result))
# str_result = str(result)
# print(type(str_result))
# print(str_result * 2)


# num = float(input("Введите число: "))
# print(num)
# print(type(num))


# Преобразование строки в число
# text_number = "123"
# number = int(text_number)
# print(number) # Вывод: 123
# # Преобразование числа с плавающей точкой в целое
# float_number = '3.14'
# integer_number = float(float_number)
# result = integer_number // 1
# print(integer_number) # Вывод: 3
# print(result) # Вывод: 3
# # Преобразование логического значения в число
# is_true = True
# number_from_boolean = int(is_true)
# print(number_from_boolean) # Вывод: 1
#
# is_false = False
# number_from_boolean = int(is_false)
# print(number_from_boolean) # Вывод: 1

# print(bool(-1000))
# print(bool(0))


# print(2 == True + True )
#
# age = 25
# age_as_text = str(age)
# print("Мне " + age_as_text + " лет")


# is_python_cool = True
# answer = str(is_python_cool)
# print("Python крутой? " + answer)


# if условие:
# Код, который выполняется, если условие истинно
# Пример
#
# money = 20
# if money >= 35:
#     # pass
#     # print("Вы можете купить колу")
#     # print("Вы можете купить колу")
#     # print("Вы можете купить колу")
#     # print("Вы можете купить колу")
# # else:
# #     print("Вы не можете купить колу")
# print("END")


# x = 10
# if x > 5:
#     print("x больше 5")
# else:
#     print("x меньше или равно 5")


# x = 15
# if x > 10:
#     print("x больше 10")
#     if x > 20:
#         print("x больше 20")
#         if x > 20:
#             print("x больше 20")
#     else:
#         print("x больше 10, но меньше или равно 20")
# else:
#     print("x меньше или равно 10")


# Определение оценки
# ball = 15
# num = 20
# if ball <= 5:
#     print("Отлично")
# elif num <= 20:
#     print("Хорошо")
# elif ball <= 30:
#     print("Удовлетворительно")
# else:
#     print("Неудовлетворительно")

# x = 10
# result = "x больше 5" if x > 5 else "x меньше или равно 5"
# print(result) # Вывод: x больше 5
#
#
# if x > 5:
#     result = "x больше 5"
# else:
#     result = "x меньше или равно 5"
#
# result = "x больше 5" if x > 5 else "x меньше или равно 5"


# Оператор and возвращает True только если оба его аргумента истинны (True).
# a = True
# b = False
# res = 10 > 5 and 20 > 10 and 10 > 20
# print(res)
#
# if res:
#     print(True)
# print('END')
#
# 1 and 1 = 1
# 1 and 0 = 0
# 0 and 1 = 0
# 0 and 0 = 0


# # Оператор or возвращает True, если хотя бы один из его аргументов истинен.
# a = True
# b = False
# print(a or b) # Выведет: True

# 1 or 1 = 2
# 1 or 0 = 1
# 0 or 1 = 1
# 0 or 0 = 0

# a = True
# b = False
# c = True
#
# if (a or b) and c:
#     print(1)

# # Оператор not инвертирует булево значение своего аргумента.
# a = False
# print(not a) # Выведет: False


a = [1, 2, 3] # Переменная `a` ссылается на список
b = a # Переменная `b` теперь тоже ссылается на тот же список
print(a)
 # Выведет: [1, 2, 3]
print(b)
 # Выведет: [1, 2, 3]
b.append(4)
 # Добавим элемент в список через `b`
print(a)
 # Выведет: [1, 2, 3, 4]
print(b)
 # Выведет: [1, 2, 3, 4]