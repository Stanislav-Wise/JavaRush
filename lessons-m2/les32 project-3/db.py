import psycopg2
from psycopg2 import OperationalError


DB_NAME = "images_db"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "db"
DB_PORT = 5432


def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except OperationalError as e:
        print(f'Ошибка подключения к БД: {e}')
        return None


def close_db(conn):
    if conn:
        conn.close()


def create_table_images():
    conn = connect_db()
    cur = conn.cursor()

    sql = """
             CREATE TABLE images (
        id SERIAL PRIMARY KEY,
        filename TEXT NOT NULL,
        original_name TEXT NOT NULL,
        size INTEGER NOT NULL,
        upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        file_type TEXT NOT NULL
    );"""
    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()


def save_images(filename, original_name, size, upload_time, file_type):
    conn = connect_db()
    cur = conn.cursor()

    sql = """
        INSERT INTO images (filename, original_name, size, upload_time, file_type)
            VALUES (%s, %s, %s, %s, %s)
    """
    cur.execute(sql, (filename, original_name, size, upload_time, file_type))
    conn.commit()

    cur.close()
    conn.close()




    #
    # CREATE TABLE images (
    #     id SERIAL PRIMARY KEY,
    #     filename TEXT NOT NULL,
    #     original_name TEXT NOT NULL,
    #     size INTEGER NOT NULL,
    #     upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    #     file_type TEXT NOT NULL
    # );