contacts = {
    "Алексей": "+7-999-123-45-67",
    "Мария": "+7-888-456-78-90",
    "Ольга": "+7-777-987-65-43"
}
#
# try:
#     name = input("Введите имя контакта: ")
#     phone = contacts[name]
#     print(f"Телефон {name}: {phone}")
# except KeyError:
#     print("Ошибка: Контакт не найден!")

name = input("Введите имя контакта: ")
phone = contacts[name]
print(f"Телефон {name}: {phone}")