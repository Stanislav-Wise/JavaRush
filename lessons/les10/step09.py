def natural_numbers():
    n = 1
    while True:
        yield n
        n += 2


naturals = natural_numbers()
for _ in range(30):
    print(next(naturals))