# try:
#     x = int(input("Введите число: "))
#     result = 10 / x
#
# except ZeroDivisionError:
#     print("Произошла неизвестная ошибка 1!")
# except ValueError:
#     print("Произошла неизвестная ошибка 1!")
# except Exception:
#     print("Произошла неизвестная ошибка.")


try:
    x = int(input("Введите число: "))
    result = 10 / x

except (ZeroDivisionError, ValueError):
    print("Произошла известная ошибка 1!")
# except ValueError:
#     print("Произошла неизвестная ошибка 1!")
except Exception:
    print("Произошла неизвестная ошибка.")
