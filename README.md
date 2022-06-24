#api_yamdb
Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
git@github.com:yandex-praktikum/api_yamdb.git

cd api_final_yatube
Cоздать и активировать виртуальное окружение:

python3 -m venv env
source venv/Scripts/activate
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

python3 manage.py migrate
Запустить проект:

python3 manage.py runserver


![]([https://img.shields.io/pypi/pyversions/p5?color=green&label=python&logo=python&logoColor=green](https://img.shields.io/badge/dynamic/xml?color=green&label=python&query=3.7&url=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-3713%2F))
