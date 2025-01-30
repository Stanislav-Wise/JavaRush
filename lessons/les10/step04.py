# lambda аргументы: выражение

#
# square = lambda x: x ** 2
# print(square(5))

#
# add = lambda a, b: a + b
# print(add(3, 7))
#
#
# # Использование с map()
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x ** 2, numbers)
# print(list(squared_numbers))


# # Использование с filter()
# numbers = [1, 2, 3, 4, 5]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))


# # Использование с sorted()
# words = ["apple", "banana", "cherry", "date"]
# sorted_words = sorted(words, key=lambda x: len(x))
# print(sorted_words)


# Передача лямбда-функции
def process_data(data, func):
    return [func(x) for x in data]

numbers = [1, 2, 3, 4, 5]
result = process_data(numbers, lambda x: x ** 3)
print(result)