# # Встроенная функция id()
# a = 10
# b = 10
# print(id(a))
# print(id(b))


# # Встроенная функция hash()
# print(hash("hello"))
# print(hash(42))
# print(hash((1, 2, 3)))
# # print(hash([1, 2, 3]))
#
# # Пример ошибки
# try:
#     hash([1, 2, 3])
# except TypeError as e:
#     print(e)


# # Встроенная функция dir()
# class MyClass:
#     def __init__(self):
#         self.name = "Alice"
#
#     def greet(self):
#         print(f"Hello, {self.name}!")
#
# obj = MyClass()
# print(dir(obj))
#
#
# Записная книжка
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


contact1 = Contact("Анна", "+79161234567")
contact2 = Contact("Анна", "+79161234567")

print(id(contact1))
print(id(contact2))

try:
    print(hash(contact1))
except TypeError as e:
    print(e)

print(dir(contact1))


# Хэшируемые контакты
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __hash__(self):
        return hash((self.name, self.phone))

    def __eq__(self, other):
        return self.name == other.name and self.phone == other.phone

contact1 = Contact("Анна", "+79161234567")
contact2 = Contact("Анна", "+79161234567")

print(hash(contact1))
print(hash(contact2))

print(contact1 == contact2)