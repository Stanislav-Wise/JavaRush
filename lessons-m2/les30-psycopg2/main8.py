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
upd_les = ('les HTML', 90)

new_les = ('les5 ErrorTest', 10)

try:
    cursor.execute("INSERT INTO java (name, grade) VALUES (%s, %s);", new_les)

    cursor.execute("UPDATE java SET first_name = %s WHERE grade < %s;", upd_les)
    conn.commit()

    print('Транзакция завершена')

except Exception as e:
    conn.rollback()
    print('Транзакция НЕ завершена')
    print(f'ОШИБКА! {e}')


cursor.close()
conn.close()