Создать виртуальное окружение  
python3 -m venv .venv  
source ./.venv/bin/activate  
  
Установка Django  
pip install django  
poetry init  
poetry add django  
  
django-admin --version
  
Создать проект  
django-admin startproject config .    
  
Создать приложение  
python manage.py startapp blog_app  
  
Запустить сервер  
python manage.py runserver  


https://sqlitebrowser.org/

Создать миграции
python manage.py makemigrations

Применить миграции
python manage.py migrate

Интерактивная консоль Django
python manage.py shell

python manage.py loaddata ./data/blog_fixture.json

python manage.py dumpdata blog_app --indent 4 > ./data/blog_post_fixture1.json


Использовать реальную БД в тесте
pytest --reuse-db
  
Установка bs4   
poetry add beautifulsoup4   
  
## Redis  
https://redis.io/download  
  
## Redis docker   
docker run -d --name redis-server -p 6379:6379 redis  
  
## Redis test  
redis-cli ping  

## Запуск worker'a
celery -A config worker --loglevel=info

## Запуск celery beat
celery -A config beat --loglevel=info

# Запрос токена
curl -X POST http://127.0.0.1:8000/api/v1/token/ -H "Content-Type: application/json" -d '{"email": "admin@mail.com", "password": "1"}'

# Обновление токена
curl -X POST http://127.0.0.1:8000/api/v1/token/refresh/ -H "Content-Type: application/json" -d '{"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2MDExMjg4NCwiaWF0IjoxNzYwMDI2NDg0LCJqdGkiOiIyZDk4YjI5NDg0YmY0ZjRkYTVlMjE5ZGM3N2ZmYzA3NSIsInVzZXJfaWQiOiIxIn0.vdw8muaBb5eX3Oj7Ycq4Y73C1_wJWFBcbQg8ERPZXdU"}'

# Создать свой Post под токеном
curl -X POST http://127.0.0.1:8000/api/v1/authors/ -H "Content-Type: application/json" -H "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYwOTc3NDcxLCJpYXQiOjE3NjA5NzcxNzEsImp0aSI6ImRhOGM0NTAyNzI5MzRiMDc4ODE2YzRlYTkzYjFhNjFkIiwidXNlcl9pZCI6IjEifQ.orcgDe8BOGuvwTkm0s5VSPvJ0FYGoTT4GdSI7gC1htw" -d '{"name": "Tanos"}'