
try:
    number = int(input("Введите число: "))
    result = 100 / number
    print(f"Результат: {result}")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except ValueError:
    print("Ошибка: введено не число!")


print("Программа завершена")

# number = int(input("Введите число: "))
# result = 100 / number
# print(f"Результат: {result}")