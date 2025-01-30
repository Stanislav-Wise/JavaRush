contacts = {
    "Алексей": "+7-999-123-45-67",
    "Мария": "+7-888-456-78-90",
    "Ольга": "+7-777-987-65-43"
}

def get_contact(name):
    """Ищет контакт в телефонной книге."""
    if name not in contacts:
        raise KeyError(f"Контакт {name} не найден!")
    return contacts[name]

def add_contact(name, phone):
    """Добавляет новый контакт в телефонную книгу."""
    if not isinstance(name, str) or not isinstance(phone, str):
        raise TypeError("Имя и телефон должны быть строками!")
    if name in contacts:
        raise ValueError(f"Контакт {name} уже существует!")
    contacts[name] = phone
    print(f"Контакт {name} успешно добавлен!")

def main():
    try:
        # Пример вызова функций
        # add_contact("Алексей", "+7-900-123-45-67")  # Ошибка: контакт уже существует
        name = input("Введите имя контакта: ")
        phone = get_contact(name)
        print(f"Телефон {name}: {phone}")
    except KeyError as e:
        print(f"Ошибка: {e}")
    except TypeError as e:
        print(f"Ошибка типа данных: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

main()