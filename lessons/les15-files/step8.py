file_obj = open("javarush.txt", "r")
data = file_obj.readline()

while data:
    print(data.strip("\n"))
    data = file_obj.readline()


file_obj.close()