import os

if os.path.isfile("javarush.txt"):
    print("Это файл")
else:
    print("Это не файл")


if os.path.isdir("old"):
    print("Это dir")
else:
    print("Это не dir")