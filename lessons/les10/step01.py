# # Простая функция
# def say_hello():
#     print("Привет, мир!")
#
#
# say_hello()
# say_hello()


# # Функция с двумя параметрами
def greet_user(name, age):
    print(f"Привет, {name}! Тебе уже {age} лет.")


print(greet_user("Нурлан", 35))
#
#
# Функция с возвращаемым значением
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 10)
print(result)