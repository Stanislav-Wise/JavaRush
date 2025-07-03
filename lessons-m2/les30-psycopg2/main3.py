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

cursor.execute("SELECT * FROM java ORDER BY id;")

row = cursor.fetchone()

print(row)
print(type(row))


row = cursor.fetchone()

print(row)
print(type(row))


row = cursor.fetchone()

print(row)
print(type(row))


row = cursor.fetchone()

if row:
    print(row)
    print(type(row))
else:
    print('Результат не найден')



cursor.close()
conn.close()