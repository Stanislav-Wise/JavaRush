def divide_numbers():
    try:
        x = int(input("Введите число: "))
        result = 100 / x
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    except ValueError:
        print("Ошибка: введено не число!")
    else:
        print(f"Результат деления: {result}")
    finally:
        print("Операция завершена.")

divide_numbers()