with open('tanos.jpeg', 'rb') as bin_file:
    data = bin_file.readline()
    while data:
        print(data)
        data = bin_file.readline()


