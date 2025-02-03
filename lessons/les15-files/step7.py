file_obj = open("javarush.txt", "r")
data = ' '

while data:
    data = file_obj.read(50)
    print(data)

file_obj.close()