file_obj = None
try:
    file_obj = open("temp.txt", "r")
    data = file_obj.read()
    print(data)
except FileNotFoundError:
    print("Ошибка: файл не найден.")
finally:
    if file_obj:
        file_obj.close()
