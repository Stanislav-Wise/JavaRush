# def check_age(age):
#     if age < 0:
#         raise ValueError("Возраст не может быть отрицательным")
#     print(f"Ваш возраст: {age}")
#
# check_age(-5)


def process_data(data):
    try:
        if not isinstance(data, list):
            raise TypeError("Ожидался список")
        if len(data) == 0:
            raise ValueError("Список пуст")
    except TypeError as e:
        raise ValueError("Ошибка обработки данных") from e
    print("Данные обработаны:", data)

try:
    process_data("not a list")
except ValueError as e:
    print(f"Произошла ошибка: {e}")