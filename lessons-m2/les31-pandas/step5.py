import pandas as pd
from step3 import get_connection
import matplotlib.pyplot as plt


connection = get_connection()
query = "SELECT * FROM java;"

df = pd.read_sql_query(query, connection)


# print('Групировака данных')
# df_group = df.groupby("grade").count()
# print(df_group)
#
#
# print('Средняя оценка')
# df_avg = df["grade"].mean()
# print(round(df_avg, 2))
#
#
# print('Групировака данных по первой букве')
# df["first_letter"] = df["name"].str[0]
# df_group_first_letter = df.groupby("first_letter")["grade"].mean()
# print(df_group_first_letter)

# df.plot(x="name", y="grade", kind="bar", title="Оценки студентов", legend=False)
# plt.xlabel("Имя")
# plt.ylabel("Оценка")
# plt.tight_layout()
# plt.show()


# df.plot(x="name", y="grade", kind="line", title="Оценки студентов", marker="o")
# plt.xlabel("Имя")
# plt.ylabel("Оценка")
# plt.tight_layout()
# plt.show()

#
# df["grade"].plot(kind="hist", bins=5, title="Гистограма Оценки студентов")
# plt.xlabel("Имя")
# plt.ylabel("Оценка")
# plt.tight_layout()
# plt.show()



df["grade"].value_counts().plot(kind="pie", autopct="%1.1f%%", title="Гистограма Оценки студентов")
plt.xlabel("Имя")
plt.ylabel("Оценка")
plt.tight_layout()
plt.show()