bin_file = open('tanos.jpeg', 'rb')

data = bin_file.read()
print(data)
print(len(data))

bin_file.close