from pathlib import Path

# path_obj = Path("/test/app2.py")

# print(path_obj.name)
# print(path_obj.parent)
# print(path_obj.suffix)
# print(path_obj.exists())

# if path_obj.exists():
#     # print(path_obj.read_text())
#     print("Объект существует")
#     if path_obj.is_file():
#         print("Это файл")
#     elif path_obj.is_dir():
#         print("Это dir")
#     else:
#         print("Это что-то другое")
# else:
#     print("File not found")

# parent_dir = path_obj.parent
# print(parent_dir)
#
# grand_dir = parent_dir.parent
# print(grand_dir)
#
# all_parent = list(path_obj.parents)
# print(all_parent)

# for item in path_obj.iterdir():
#     print(item.name)

# path_obj.mkdir()

# path_obj.mkdir(exist_ok=True, parents=True) # Создание директории
# path_obj.rmdir()  # Удаление директории

# with path_obj.open(mode='w', encoding='utf-8') as f:
#     f.write("print('hello world')")
#

# print(path_obj.is_absolute())
path_obj = Path("temp/test/")
path_obj1 = path_obj /'app2.py'
print(path_obj1)