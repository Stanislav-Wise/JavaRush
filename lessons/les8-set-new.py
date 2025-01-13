# friends = {"Алиса", "Боб", "Алиса", "Боб", "Катя"}
# print(friends)
# print(type(friends))
#
# friends = set()
# print(friends)
# print(type(friends))


# friends_list = ("Алиса", "Боб", "Катя", "Алиса", "Боб", "Катя", 'Иван')
# unique_friends = set(friends_list)
# print(unique_friends)
# print(len(unique_friends))
#
# friends = set()
# if not friends:
#     print("Множество пустое")
# else:
#     print("Множество не пустое")


#
# if  "Боб123" in unique_friends:
#     print("Yes")
# else:
#     print("No")
#
# for item in unique_friends:
#     print(item)


# friends = {"Алиса", "Боб", "Алиса", "Боб", "Катя"}
# print(friends)
# sort_set = sorted(friends)
# print(sort_set)
#
# friends_all = {"Алиса", "Боб", "Катя", "Дима", "Елена"}
# close_friends = {"Алиса", "Катя"}
# # print(close_friends <= friends_all)
# # print(close_friends.issubset(friends_all))
#
# print(friends_all >= close_friends)
#
# friends_all = {"Алиса", "Боб", "Катя", "Дима", "Елена"}
# friends_k = set()
#
# for friend in friends_all:
#     if friend.startswith("К"):
#         friends_k.add(friend)
#
# print(friends_k)
# print(friends_k.issubset(friends_all))

#
# my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_set = set(filter(lambda x: x % 2 == 0, my_set))
# print(even_set) # Вывод: {2, 4, 6, 8, 10}

# friends = {"Алиса", "Боб"}
# friends.add("Катя")
# friends.add("Катя123")
# friends.add("Катя")
# print(friends)

# friends = {"Алиса", "Боб", "Катя"}
# friends.remove("Боб")
# print(friends)
#
# friends.remove("Дмитрий")
# print(friends)

# friends = {"Алиса", "Боб", "Катя"}
# friends.discard("Боб")
# print(friends)
# friends.discard("Дмитрий")
# print(friends)


# friends = {"Алиса", "Боб", "Катя"}
# removed = friends.pop()
# print(f"Удалено: {removed}")
# print(f"Осталось: {friends}")


# friends = {"Алиса", "Боб", "Катя"}
# friends.clear()
# print(friends)

# friends = {"Алиса", "Боб"}
# new_friends = {"Катя", "Дмитрий", "Боб"}
# friends.update(new_friends)
# print(friends)

#
# friends = {"Алиса", "Боб", "Катя", "Дима"}
# for friend in friends:
#     if friend.startswith("А"):
#         print(f"{friend} - имя начинается с буквы 'А'.")

# friends = {"Алиса", "Боб", "Катя", "Дима"}
# for index, friend in enumerate(friends, start=1):
#     print(f"Индекс: {index}, Имя: {friend}")


# nested_friends = {("Алиса", "Боб"), ("Катя", "Дима")}
# for f1, f2 in nested_friends:
#     print(f"Пара друзей: {f1} {f2}")



# my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_set = {x for x in my_set if x % 2 == 0}
# print(even_set)


# my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, "apple", "banana"}
# even_set = {x.upper() for x in my_set if type(x) == str}
# print(even_set)


group_a = {"Алиса", "Боб", "Катя"}
group_b = {"Дима", "Катя", "Елена"}

# union_result = group_a | group_b
# print("Объединение (|):", union_result)
#
# union_result_method = group_a.union(group_b)
# print("Объединение (union):", union_result_method)
#
#
# intersection_result = group_a & group_b
# print("Пересечение (&):", intersection_result)
#
# intersection_result_method = group_a.intersection(group_b)
# print("Пересечение (intersection):", intersection_result_method)

# difference_result = group_a - group_b
# print("Разность (-):", difference_result)
#
# difference_result_method = group_a.difference(group_b)
# print("Разность (difference):", difference_result_method)

symmetric_difference_result = group_a ^ group_b
print("Симметрическая разность (^):", symmetric_difference_result)

symmetric_difference_method = group_a.symmetric_difference(group_b)
print("Симметрическая разность (symmetric_difference):", symmetric_difference_method)