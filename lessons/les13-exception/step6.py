# numbers = [1, 2, 3]
# try:
#     print(numbers[2])  # Ошибка: индекса 5 нет
# except IndexError as e:
#     print(f"Ошибка: {e}")


# my_dict = {"a": 1, "b": 2}
# try:
#     print(my_dict["c"])  # Ошибка: ключа "c" нет
# except KeyError as e:
#     print(f"Ошибка: ключ {e} отсутствует в словаре")


try:
    number = int("abc")  # Ошибка: строку нельзя преобразовать в число
except ValueError as e:
    print(f"Ошибка: {e}")