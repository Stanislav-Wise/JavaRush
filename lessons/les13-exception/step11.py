class NegativeValueError(Exception):
    """Исключение для отрицательных значений."""
    pass


class MyValueError(NegativeValueError):
    """Исключение для отрицательных значений."""
    pass


class NewValueError(NegativeValueError):
    """Исключение для отрицательных значений."""
    pass
#
#
# def check_value(value):
#     if value < 0:
#         raise NegativeValueError(f"Значение {value} не может быть отрицательным!")
#     print(f"Значение корректно: {value}")
#
# try:
#     check_value(-10)
# except NegativeValueError as e:
#     print(f"Ошибка: {e}")


class InvalidContactError(Exception):
    """Исключение для некорректных данных контакта."""
    pass


def validate_contact(name, phone):
    """Проверяет корректность данных контакта."""
    if not isinstance(name, str) or not name:
        raise InvalidContactError("Имя контакта должно быть непустой строкой!")
    if not isinstance(phone, str) or len(phone) < 7:
        raise InvalidContactError("Номер телефона должен быть строкой длиной от 7 символов!")

def add_contact(name, phone):
    """Добавляет контакт с проверкой данных."""
    try:
        validate_contact(name, phone)
        if name in contacts:
            raise ValueError(f"Контакт {name} уже существует!")
        contacts[name] = phone
    except (InvalidContactError, ValueError) as e:
        print(f"Ошибка: {e}")
        raise
    else:
        print(f"Контакт {name} успешно добавлен!")

