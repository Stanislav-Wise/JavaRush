def read_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
    except FileNotFoundError:
        print("Ошибка: файл не найден.")
    except IOError:
        print("Ошибка: проблемы с доступом к файлу.")
    else:
        print("Содержимое файла:")
        print(content)
    finally:
        if 'file' in locals() and not file.closed:
            file.close()
            print("Файл закрыт.")