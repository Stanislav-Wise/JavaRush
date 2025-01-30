def log_method_call(func):
    def wrapper(self, *args, **kwargs):
        print(f"Вызов метода {func.__name__} с аргументами {args}, {kwargs}")
        return func(self, *args, **kwargs)
    return wrapper

class MyClass:
    @log_method_call
    def say_hello(self):
        print("Hello from MyClass!")

obj = MyClass()
obj.say_hello()