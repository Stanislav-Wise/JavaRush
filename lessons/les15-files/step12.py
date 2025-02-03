lines_to_save = [
    "Установка PyCharm.\n",
    "Установка Python.\n",
    "Создание проекта.\n"
]

file_obj = open("temp2.txt", "a")
file_obj.writelines(lines_to_save)
file_obj.close()