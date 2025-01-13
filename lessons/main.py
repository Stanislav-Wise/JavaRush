import random
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
def find_max(a, b):
  if a > b or b > a:
    return (max(a, b))
  elif a == b:
    return(random.randint(a, b))
  return max
result = find_max(a, b)
print(result)


# def find_max(a, b):
#  return a if a >= b else b
#
# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))
#
# max_number = find_max(num1, num2)
# print("Большее число:", max_number)