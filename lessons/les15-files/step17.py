bin_data = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00\x84\x00\n'

with open('tanos1.jpeg', 'ab') as bin_file:
    bin_file.write(bin_data)



