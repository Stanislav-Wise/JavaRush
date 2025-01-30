def generator1():
    yield from range(3)
    yield from "ABC"

# Использование
# for value in generator1():
#     print(value)


gen = generator1()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))