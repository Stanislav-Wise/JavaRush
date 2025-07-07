import csv
import psycopg2
from step1 import read_csv


POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres"
POSTGRES_DB = "dvdrental"
PORT = 5432
HOST = "localhost"


def insert_student(data):
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

                cursor.executemany(
                    "INSERT INTO java (name, grade) VALUES (%s, %s);",
                    data
                )

                print(f'{cursor.rowcount} rows inserted.')

    except Exception as e:
        print('Общая ошибка')
        print(f'ОШИБКА! {e}')


if __name__ == '__main__':
    student_data = read_csv()
    insert_student(student_data)
