
# Запуск uvicorn в терминале
uvicorn main:app --reload

## alembic посмотреть версию сервиса после установки
alembic --version

## alembic - инициализация проекта в директорию alembic
alembic init alembic

## alembic  - текущая версия
alembic current

## alembic  - создать новую миграцию с описанием "init"
alembic revision --autogenerate -m "init"

## alembic  - применить миграцию 
alembic upgrade head

## alembic  - посмотреть историю миграций
alembic history
alembic history --verbose

## alembic  - откатиться на 1 миграцию назад
alembic downgrade -1

## alembic  - откатиться на миграцию bcd717f367d7
alembic downgrade bcd717f367d7

## alembic  - откатиться в начало
alembic downgrade base