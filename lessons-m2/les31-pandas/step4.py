import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import psycopg2
from step3 import get_connection


connection = get_connection()
query = "SELECT id, name, grade FROM java;"

df = pd.read_sql_query(query, connection)

# print(df)
connection.close()

print(df.head())
print(df.columns)
print(df.dtypes)
print(df.describe())

df.to_csv("student_output_csv.csv", index=False)