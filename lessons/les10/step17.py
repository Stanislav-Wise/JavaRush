# import datetime

# d = datetime.date(2025, 1, 19)
# print(type(d))
# print(d)
#
# today = datetime.date.today()
# print(today)
#
# print(today.year)
# print(today.month)
# print(today.day)
#
# t = datetime.time(14, 30, 45)
# print(t.hour)
# print(t.minute)
# print(t.second)
#
# dt = datetime.datetime(2025, 1, 16, 14, 30, 45)
# print(dt)
#
# now = datetime.datetime.now()
# print(now)

# delta = datetime.timedelta(days=5, hours=3)
# print(delta)
#
#
# d = datetime.date(2025, 1, 16)
# new_date = d + delta
# print(new_date)


import datetime

dt = datetime.datetime(2023, 5, 24, 14, 30, 45)

# Форматирование даты и времени
formatted_dt = dt.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_dt) # Вывод: 2023-05-24 14:30:45
# Форматирование только даты
formatted_date = dt.strftime("%d-%m-%Y")
print(formatted_date) # Вывод: 24-05-2023
# Форматирование только времени
formatted_time = dt.strftime("%H:%M:%S")
print(formatted_time) # Вывод: 14:30:45