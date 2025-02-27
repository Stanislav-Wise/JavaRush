python -m venv .venv  - Создание виртуального окружения  
source ./.venv/bin/activate - Активация виртуального окружения  в Linux и MacOS  
.\.venv\Scripts\activate - Активация виртуального окружения в Windows 
  
  
pip install flask - Установка библиотеки Flask  
pip install requests==2.26.0 - Установка библиотеки requests версия 2.26.0  
pip list - Список установленных библиотек  
  
pip install --upgrade requests - Обновление библиотеки requests  
   
pip uninstall pyyaml - Удаление библиотеки pyyaml    
  
pip freeze > requirements.txt - Сохранение списка установленных библиотек в requirements.txt   
  
pip install -r requirements.txt - Установка библиотек из requirements.txt   
    
    
https://python-poetry.org/docs/#installing-with-the-official-installer  
документация poetry  
  
curl -sSL https://install.python-poetry.org | python3 -    Установка poetry  
  
poetry new new_project - Создание нового проекта  
poetry init - Инициализация проекта  
  
xx.yy.zz  
xx -  мажорная версия  
yy - минорная версия  
zz - патч  
  
  
poetry add requests - Установка библиотеки requests  
poetry add flask - Установка библиотеки Flask  
  
"pyyaml (>6.0.2,<=6.7.0)"   - , - это логическое И  
"pyyaml==6.0.1",  
"pyyaml (^6.0.2)"  - тоже, что и "pyyaml (>=6.0.2,<7.0.0)"   
"pyyaml (~6.0.2)"  - тоже, что и "pyyaml (>=6.0.2,<6.1.0)"   
"pyyaml (6.*.*)"  - тоже, что и "pyyaml (>=6.0.2,<7.0.0)"   
python = "3.9 || 3.11"  - || - логическое ИЛИ  
  
  
poetry install - Установка зависимостей  
  
poetry update - Обновление зависимостей   
  
poetry remove flask - Удаление библиотеки Flask  
  
poetry add --group dev pytest - Установка библиотеки pytest в группу dev  
  
poetry add flask@3.0.1 - Установка библиотеки Flask версии 3.0.1  
  
poetry show - Просмотр списка установленных библиотек  
  
poetry check - Проверка списка установленных библиотек на наличие ошибок  
  
poetry env info - Просмотр информации о виртуальном окружении  
  
poetry shell - Активация виртуального окружения    
  
poetry install --without dev - Установка зависимостей без группы dev  
  
poetry install --only dev - Установка зависимостей только для группы dev  
