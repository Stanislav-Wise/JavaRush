file_obj = open("javarush.txt", "w")

for _ in range(5):
    data = file_obj.write("1qaz\n")



file_obj.close()