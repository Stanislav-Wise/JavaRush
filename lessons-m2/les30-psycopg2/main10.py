import psycopg2
from psycopg2 import sql

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

try:
    with psycopg2.connect(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        dbname=POSTGRES_DB,
        host=HOST,
        port=PORT
    ) as conn:



        print("Успешное подключение к БД ")

        with conn.cursor() as cursor:

            cursor.execute("SELECT * FROM java;")

            rows = cursor.fetchall()
            for row in rows:
                print(row)


# except OperationalError as e:
#     print('Ошибка подключения к БД')
#     print(f'ОШИБКА! {e}')
#
# except ProgrammingError as e:
#     print('Ошибка в SQL запросе')
#     print(f'ОШИБКА! {e}')
#
except Exception as e:
    print('Общая ошибка')
    print(f'ОШИБКА! {e}')

