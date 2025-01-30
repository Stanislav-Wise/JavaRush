# Базовый класс исключений
class ApplicationError(Exception):
    """Базовый класс для исключений приложения."""
    pass

# Исключения для ошибок валидации
class ValidationError(ApplicationError):
    """Ошибка валидации данных."""
    pass

class InvalidNameError(ValidationError):
    """Ошибка некорректного имени."""
    pass

class InvalidPhoneError(ValidationError):
    """Ошибка некорректного номера телефона."""
    pass

# Исключения для работы с базой данных
class DatabaseError(ApplicationError):
    """Ошибка при работе с базой данных."""
    pass



def validate_name(name):
    """Проверяет корректность имени."""
    if not isinstance(name, str) or not name:
        raise InvalidNameError("Имя контакта должно быть непустой строкой!")

def validate_phone(phone):
    """Проверяет корректность номера телефона."""
    if not isinstance(phone, str) or len(phone) < 7:
        raise InvalidPhoneError("Номер телефона должен быть строкой длиной от 7 символов!")

def validate_contact(name, phone):
    """Проверяет корректность имени и телефона."""
    validate_name(name)
    validate_phone(phone)

def add_contact(name, phone):
    """Добавляет контакт с проверкой данных."""
    try:
        validate_contact(name, phone)
        if name in contacts:
            raise DatabaseError(f"Контакт {name} уже существует!")
        contacts[name] = phone
    except ApplicationError as e:
        print(f"Ошибка: {e}")
        # logging.error("Ошибка при добавлении контакта:\n%s", traceback.format_exc())
        raise
    else:
        print(f"Контакт {name} успешно добавлен!")



try:
    add_contact("Алексей", "12345")  # Неверный номер
except InvalidPhoneError as e:
    print(f"Ошибка номера телефона: {e}")
except ValidationError as e:
    print(f"Ошибка валидации: {e}")
except ApplicationError as e:
    print(f"Общая ошибка приложения: {e}")
