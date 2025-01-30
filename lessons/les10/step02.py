# # Присвоение функции переменной
# def greet():
#     return "Привет, мир!"
#
#
# message = greet
# print(message())
#
# my_print = print
# my_print(message())


# # Функция как аргумент
# def shout(text):
#     return text.upper()
#
# def whisper(text):
#     return text.lower()
#
# def process_message(func, message):
#     return func(message)
#
#
# print(process_message(shout, "Привет, Python!"))
# print(process_message(whisper, "Привет, Python!"))
#
#
# Возвращение функции
def multiplier(factor):
    def multiply_by(value):
        return value * factor
    return multiply_by


times_two = multiplier(2)
times_five = multiplier(5)

print(times_two(10))  # 20
print(times_five(10))  # 50