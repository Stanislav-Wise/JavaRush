# print('Как тебя зовут')
# name_1 = input()
# print('Пока, ' + name_1)
#
# print('А тебя как зовут?')
# name_2 = input()
# print('Пока, ' + name_2)
#
# print('А как зовут твоего пса?')
# name_3 = input()
# print('Привет, ' + name_3)


# new_greet = greet
#
# new_greet('Как тебя зовут?', 21)
#
# new_greet('А тебя как зовут?', 30)
#
# new_greet('А как зовут твоего пса?', 2)

# my_print = print
#
# my_print(12345)
# import random
#
# AGE = 123
#
# greeting = 'Привет'
#
# def greet(message, age, pet=False):
#     global greeting
#     name = input(f'{message}: ')
#     greeting = 'Пока'
#     print(f'local {greeting}')
#     if pet:
#         return f'{greeting} {name}, тебе {age * 5} лет'
#     return f'{greeting} {name}, тебе {age} лет'
#
#
# print(f"global {greeting}")
# res_1 = greet(age=21, message='Как тебя зовут?')
#
# res_2 = greet(age=30, message='А тебя как зовут?')
#
# res_3 = greet('А как зовут твоего пса?', 2, pet=True)
#
# print(res_1, res_2, res_3, sep='\n')
# print(f"global {greeting}")



#
# def greet(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     # result = ''
#     # for name in args:
#     #     result += f"Привет, {name}\n"
#     # return result
#     # # return f'{greeting} {name}, тебе {age} лет'
#
#
# res_1 = greet(21, 'Как тебя зовут?', pet=True)
# print(res_1)
#


def greet(message: str, age: int, pet: bool = False) -> str | None:
    """ Функция приветствия пользователей. """
    name = input(f'{message}: ')
    greeting = 'Пока'
    if pet:
        return f'{greeting} {name}, тебе {age * 5} лет'
    return f'{greeting} {name}, тебе {age} лет'


help(greet)
#
# res_1 = greet(age='ten', message='Как тебя зовут?')
#
# res_2 = greet(age=30, message='А тебя как зовут?')
#
# res_3 = greet('А как зовут твоего пса?', 2, pet=True)
#
# print(res_1, res_2, res_3, sep='\n')
