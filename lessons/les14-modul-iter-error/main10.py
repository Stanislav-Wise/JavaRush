class CustomList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        """
        Возвращает элемент по индексу, например obj[index].
        """
        return self.data[index - 1]

    def __setitem__(self, index, value):
        """
        Устанавливает значение элемента по индексу, например obj[index] = value.
        """
        self.data[index] = value * 10

    def __delitem__(self, index):
        """
        Удаляет элемент по индексу, например del obj[index].
        """
        del self.data[index + 1]

    def __repr__(self):
        """
        'Официальное' строковое представление объекта,
        полезно при выводе в REPL или для отладки.
        """
        return repr(self.data)


c_list = CustomList([10, 20, 30])
print(c_list[1])

c_list[1] = 99
print(c_list)

del c_list[0]
print(c_list)