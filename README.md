<h1 align="center">Educational project: api_yamdb</h1>
RestAPI for YaMDb service - database of movies, books, music reviews
<h2 align="left">About</h2>
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

