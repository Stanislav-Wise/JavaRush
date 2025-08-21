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