import os

if os.path.exists("javarush_copy.txt"):
    os.remove("javarush_copy.txt")
else:
    print("File not found")