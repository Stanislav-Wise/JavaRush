class SuperList(list):
    def __setitem__(self, index, value):
        """
        Если index >= len(self), добавляем элемент в конец.
        Если index < 0 и выходит за границы, вставляем элемент в начало.
        Иначе - обычное поведение.
        """
        if index >= len(self):
            super().append(value)
        elif index < 0 and abs(index) > len(self):
            super().insert(0, value)
        else:
            super().__setitem__(index, value)


sl = SuperList([1, 2, 3])
sl[5] = 99
print(sl)


sl[-10] = 111
print(sl)