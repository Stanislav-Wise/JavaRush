import psycopg2


print("Всё установлено")

# POSTGRES_USER = "postgres"
# POSTGRES_PASSWORD = "postgres"
# POSTGRES_DB = "postgres"
# PORT = 5432
# HOST = "localhost"

POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres"
POSTGRES_DB = "dvdrental"
PORT = 5432
HOST = "localhost"

conn = psycopg2.connect(
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    dbname=POSTGRES_DB,
    host=HOST,
    port=PORT
)

print("Успешное подключение к БД ")


cursor = conn.cursor()

cursor.execute("SELECT * FROM java;")

rows = cursor.fetchall()

print(rows)
print(type(rows))

for row in rows:
    print(row)

cursor.close()
conn.close()