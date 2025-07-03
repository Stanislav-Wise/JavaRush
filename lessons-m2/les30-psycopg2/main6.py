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

new_les = ('les4 Python', 100)
cursor.execute("INSERT INTO java (name, grade) VALUES (%s, %s);", new_les)

conn.commit()

cursor.close()
conn.close()