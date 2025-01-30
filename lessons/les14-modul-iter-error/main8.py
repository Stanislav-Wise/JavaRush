def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


for num in my_range(1, 5):
    print(num)