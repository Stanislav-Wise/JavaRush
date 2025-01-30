class InvalidContactError(Exception):
    """Исключение для некорректных данных контакта."""
    def __init__(self, field, value, message="Некорректное значение"):
        self.field = field  # Поле, в котором произошла ошибка
        self.value = value  # Некорректное значение
        self.message = f"{message}: {field} -> {value}"
        super().__init__(self.message)  # Передаём сообщение в базовый класс

    def log_error(self):
        """Возвращает строку для логирования."""
        return f"Ошибка в поле {self.field}: значение {self.value}"


try:
    raise InvalidContactError("Телефон", "12345")
except InvalidContactError as e:
    print(e)  # Вывод: Некорректное значение: Телефон -> 12345
    print(e.log_error())