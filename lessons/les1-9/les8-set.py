# friends = {"Bob", "Rolf", "Anne"}
# print(friends)
# print(type(friends))

# names = ("Bob", "Rolf", "Anne", "Bob", "Rolf", "Anne")
# # names = 'Bob'
# print(names)
# friends = set(names)
# print(friends)

# friends = set()
# print(friends)
# print(type(friends))

# friends = {"Bob", "Rolf", "Anne", "John", "Mary", "Serj"}
# friends = set()
# print(friends)
# print(len(friends))

# if friends:
#     print('A lot of people')
# else:
#     print('Not so many people')

# friends.add("Smith")
# print(friends)

# friends.add("Bob")
# print(friends)

# if "Bob" in friends:
#     friends.remove("Bob")
#     print(friends)
# else:
#     print('Вы не дружите с Бобом')

# friends.discard("Serj")
# print(friends)
#
# friends.discard("Serj")
# print(friends)
#
# name = friends.pop()
# print(friends)
# print(name)
#
# friends.update(["Ivan"])
# print(friends)

# friends.clear()
# print(friends)

# new_friends = {"Bob", "Rolf", '123'}
# print(new_friends)
#
# print(new_friends <= friends)
# print(new_friends.issubset(friends))

# Только четные элементы
# my_set = [1, 2, 4, 4, 5, 6, 7, 8, 8, 10]
# even_set = {x for x in my_set if x % 2 == 0}
# print(even_set) # Вывод: {2, 4, 6, 8, 10}


# Только строки
# my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, "apple", "banana"}
# even_set = {x for x in my_set if type(x) == str}
# print(even_set) # Вывод: {"apple", "banana"}}

# for name in enumerate(friends):
#     print(name)

friends = {"Bob", "Rolf", "Anne", "John"}
friends_2 = {"Anne", "John", "Mary", "Serj"}

# friends_new = friends.union(friends_2)
friends_new = friends | friends_2
print(friends_new)

friends_new = friends.intersection(friends_2)
# friends_new = friends & friends_2
print(friends_new)

# friends_new = friends.difference(friends_2)
friends_new = friends - friends_2
print(friends_new)

friends_new = friends.symmetric_difference(friends_2)
# friends_new = friends ^ friends_2
print(friends_new)