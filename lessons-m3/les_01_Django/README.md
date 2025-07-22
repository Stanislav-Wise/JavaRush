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

