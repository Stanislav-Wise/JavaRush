import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

# print("Всё работает")


def get_connection():
    connection = psycopg2.connect(
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        dbname=os.getenv("POSTGRES_DB"),
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
    )

    return connection


if __name__ == '__main__':
    conn = get_connection()
    print("Успешно подключился")
    conn.close()