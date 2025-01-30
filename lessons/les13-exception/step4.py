contacts = {
    "Алексей": "+7-999-123-45-67",
    "Мария": "+7-888-456-78-90",
    "Ольга": "+7-777-987-65-43"
}

def get_contact(name):
    return contacts[name]

def print_contact(name):
    phone = get_contact(name)
    print(f"Телефон {name}: {phone}")

def main():
    name = input("Введите имя контакта: ")
    print_contact(name)

main()