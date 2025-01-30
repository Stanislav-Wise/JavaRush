def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(num_times=3)
def say_hello():
    print("Hello!")

say_hello()