https://git-scm.com/downloads
brew install git
sudo apt install git


git --version   - Проверка версии

Настройки Гита - делается 1 раз на ПК
git config --global user.name "Stanislav"
git config --global user.email "stanislav@gmail.com"

Необязательные настройки
git config --global color.ui auto  - цветовая схема
git config --global core.editor nano

Проверка настроек
git config --global --list

Инициализация проекта git
git init

Проверка статуса
git status

Добавили файл для отслеживания
git add ./README.md

Добавить все файлы для отслеживания
git add .

Сделали коммит
git commit -m "Добавлен README"


Добавить и сделать коммит
git commit -am "Обновлены файлы"

Посмотреть историю
git log

Посмотреть историю в одну строку
git log --oneline


Ссылка на github
https://github.com/

Показать ветки
git branch

Сделать главной ветку main
git branch -M main

Добавили удаленный репозиторий 
git remote add origin https://github.com/Stanislav-Wise/les17_git.git

Отправили в удлаенный репозиторий
git push -u origin main

Склонировать репозиторий
git clone https://github.com/Stanislav-Wise/testsite.git

Скачать с github
git pull

Создать новую ветку new2
git branch new2

Переключиться на ветку new2
git checkout new2
или
git switch new2   - более новый способ
