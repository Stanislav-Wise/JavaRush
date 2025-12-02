from db.session import engine


def main():
    print('Connecting to database...')

    with engine.connect() as connection:
        print('Соединение успешно установлено.')

        result = connection.execute(text("SELECT 1"))

        row = result.fetchone()

        print(f'Результат запроса {row[0]}')


    print('Проверка завершена. Соединение закрыто')


if __name__ == '__main__':
    from sqlalchemy import text
    main()