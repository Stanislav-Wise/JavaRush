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

upd_les = ('les HTML, CSS', 75)
cursor.execute("UPDATE java SET name = %s WHERE grade < %s;", upd_les)

conn.commit()

cursor.close()
conn.close()