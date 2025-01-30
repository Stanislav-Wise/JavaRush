class ApplicationError(Exception):
    pass

class ValueTooLargeError(ApplicationError):
    pass

class NegativeValueError(ApplicationError):
    pass


# ... (код, вызывающий исключение)
try:
    # ...
except NegativeValueError as e:
    print(f"Значение отрицательное: {e}")
except ValueTooLargeError as e:
    print(f"Значение слишком большое: {e}")
except ApplicationError as e:
    print(f"Общее исключение приложения: {e}")
except Exception as e:
    print(f"Непредвиденная ошибка: {e}")
