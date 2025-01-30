def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1


counter = count_up_to(5)

for item in counter:
    print(item)


for item in count_up_to(5):
    print(item)

# print(counter)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# for _ in range(4):
#     print(next(counter))