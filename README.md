<h1 align="center">Educational project: api_yamdb</h1>
RestAPI for YaMDb service - database of movies, books, music reviews
<h2 align="left">About</h2>
API for the YaMDb service. Allows you to work with:
Reviews (Get a list of all reviews, create a new review, get a review by id, partially update a review by id, delete a review by id)

- **Review comments** (Get list of all review comments by id, create new review comment, get review comment by id, partially update review comment by id, delete review comment by id)

- **JWT token** Sending confirmation_code to the given email, receiving JWT token in exchange for email and confirmation_code

- **Users** Get a list of all users, create a user, get a user by username, change user details by username, delete a user by username, get their account details, change their account details

- __**Categories (types) of works**__ Get a list of all categories, create a category, delete a category

- _**Genre**_ categories Get a list of all genres, create a genre, delete a genre

- **Reviewed** artworks Get a list of all items, create a review item, item info, update item info, delete item



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

