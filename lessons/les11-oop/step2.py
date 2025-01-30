class Fruit:
    pass


a = Fruit()
b = Fruit()


a.name = 'apple'
b.name = 'banana'

a.weight = 100
b.weight = 200

print(a.name)
print(b.name)


a.weight -= 50
print(a.weight)

# c = Fruit()
# print(c.weight)

#
# print(Fruit().name)