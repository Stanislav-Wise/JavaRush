with open('tanos.jpeg', 'rb') as bin_file:
    data = bin_file.read(100)

print(data)
print(len(data))
