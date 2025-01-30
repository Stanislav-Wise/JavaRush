class ApplicationError(Exception):
    """Базовый класс для всех пользовательских исключений."""
    def __init__(self, message=None):
        super().__init__(message)



try:
    raise ApplicationError("Произошла ошибка в приложении!")
except ApplicationError as e:
    print(e)