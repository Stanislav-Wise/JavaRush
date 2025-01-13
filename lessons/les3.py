# # # Базовый пример:
# #
# # name = "Alice 123"
# # greeting = "Привет, {}!".format(name)
# # print(greeting)  # Вывод: Привет, Alice!
#
#
# # Простой пример:
# age = 35
# print(f"Мне {age} лет.") # Вывод: Мне 30 лет.
# # Пример с форматированием чисел:
# price = 123.456
# print(f"Цена: ${price:.2f}") # Вывод: Цена: $123.46
# # Выражения внутри фигурных скобок:
# radius = 5
# pi = 3.14159
# area = pi * radius**2
# print(f"Площадь круга с радиусом {pi * radius**2} равна {area:.2f}")
# # Вывод: Площадь круга с радиусом 5 равна 78.54

# print(1, 2, 3, 4, 5, sep='---', end='!!!')
# print(2, end="qaz")
# print(3, end='+++')
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# num = 9
#
# while num > 10:
#     print(f"{num} больше 10")
#     num -= 1
#
# print('END')


# for item in 1, 2, 3, 7, 9, 4, 0, 'qwerty', True, 6.09:
#     print(item)
# start = 30
# stop = -1
# step = -3
# numbers = range(start, stop, step)
# print(*numbers)

# for i in range(1, 10):
#     print(i)

#
# for _ in range(10):
#     print(123)

# num = 20

# while num > 10:
#     num -= 1
#     if num == 13 or num == 16:
#         continue
#     print(f"{num} больше 10")
# else:
#     print('Вышли по else')
#
# print('END')
#
#
# num = 20
# flag = True
# while flag:
#
#     print(num)
#     num -= 1
#     if num == 10:
#         flag = False
# print('END')


# n = 5 # Размер таблицы
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(f"{i + 1:^15} ** {j} = {i * j}", end='\t')
#         break
#     print() # Переход на новую строку
#
# print('END')

# %(asctime)-24s| %(levelname)-8s| %(name)-12s

ascitime = "2024-12-05 19:45:56"
levelname = "INFO"
name = "MyLogger"
format_log = f"{ascitime:<24}| {levelname:<8}| {name:<12}"
format_log1 = f"{ascitime:<24}| {levelname:<8}| {name:<12}"
format_log2 = f"{ascitime:<24}| {levelname:<8}| {name:<12}"
format_log3 = f"{ascitime:<24}| {levelname:<8}| {name:<12}"
print(format_log)
print(format_log1)
print(format_log2)
print(format_log3)
