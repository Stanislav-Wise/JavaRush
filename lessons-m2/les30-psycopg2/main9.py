import psycopg2
from psycopg2 import OperationalError, ProgrammingError, IntegrityError, DatabaseError

print("Всё установлено")

# POSTGRES_USER = "postgres"
# POSTGRES_PASSWORD = "postgres"
# POSTGRES_DB = "postgres"
# PORT = 5432
# HOST = "localhost"

POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres"
POSTGRES_DB = "dvdrental"
PORT = 5431
HOST = "localhost"

try:
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

    cursor.close()
    conn.close()

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

