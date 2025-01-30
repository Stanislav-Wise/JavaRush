def my_decorator(func):
    def wrapper():
        print("Выполняется до функции")
        func()
        print("Выполняется после функции")
    return wrapper

def my_decorator1(func):
    def wrapper():
        print("Выполняется до функции1")
        func()
        print("Выполняется после функции2")
    return wrapper


@my_decorator1
@my_decorator
def say_hello():
    print("Hello!")

say_hello()


@my_decorator
def say_hello_1():
    print("Hello_1!")


say_hello_1()