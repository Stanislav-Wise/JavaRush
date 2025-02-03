import os
import shutil


print(os.getcwd())

os.chdir("/home/stanislav/PycharmProjects/JavaRush/lessons/")

print(os.getcwd())


items = os.listdir()

print(items)