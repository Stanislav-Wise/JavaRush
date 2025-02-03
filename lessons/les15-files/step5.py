file_obj = open("javarush.txt", "r")
data = file_obj.readlines()
file_obj.close()

# for line in data:
#     print(line)

print(data[2])