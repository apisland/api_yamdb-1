# Educational project: api_custom_imdb
RestAPI for Custom Imdb service - database of movies, books, music reviews
## About
API for the Custom IMDB service. Allows you to work with:

- **_Reviews_** Get a list of all reviews, create a new review, get a review by id, partially update a review by id, delete a review by id

- **_Review comments_** Get list of all review comments by id, create new review comment, get review comment by id, partially update review comment by id, delete review comment by id

- **_JWT token_** Sending confirmation_code to the given email, receiving JWT token in exchange for email and confirmation_code

- **_Users_** Get a list of all users, create a user, get a user by username, change user details by username, delete a user by username, get their account details, change their account details

- **_Categories (types) of works_** Get a list of all categories, create a category, delete a category

- **_Genre categories_** Get a list of all genres, create a genre, delete a genre

- **_Reviewed artworks_** Get a list of all items, create a review item, item info, update item info, delete item


## [Documentation(ru)](api_custom_imdb/static/redoc.yaml)


## How to start:
- Clone the repository and change directory into it on the command line:
```
git@github.com:Alastor047/api_custom_imdb.git
```
```
cd api_final_yatube
```
- Create and activate virtual environment:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
- Install requirements from a file **requirements.txt**:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
- Run migrations:
```
python manage.py migrate
```
- Upload CSV files for your database on __api_yamdb/api_yamdb/static/data/__ and use script:
```
python manage.py load_csv_data
```
- Start project:
```
python manage.py runserver
```
## Endpoints for example
- Create User        http://127.0.0.1:8000/api/v1/auth/signup/
```
{ "email": "string", "username": "string" }
```
- Get Jwt Token      http://127.0.0.1:8000/api/v1/auth/token/
```
{ "username": "string", "confirmation_code": "string" }
```
- Category List      http://127.0.0.1:8000/api/v1/categories/
- Genre List         http://127.0.0.1:8000/api/v1/genres/
- Title List         http://127.0.0.1:8000/api/v1/titles/
- Review List        http://127.0.0.1:8000/api/v1/titles/1/reviews/
- Comment List       http://127.0.0.1:8000/api/v1/titles/1/reviews/1/comments/
- User List          http://127.0.0.1:8000/api/v1/users/
- User self profile  http://127.0.0.1:8000/api/v1/users/me/
- _You can also add the id number to the end of the **List-endpoint** path to get a separate instance as shown here:_
http://127.0.0.1:8000/api/v1/titles/1/reviews/1
###### You will see this response:
![Response](https://user-images.githubusercontent.com/99352898/175463539-8f316740-144f-40b6-943e-66305e04d46c.jpg)

## Collaborators:
[Andrey Kruglov](https://github.com/Alastor047) |
[Valentin Klimov](https://github.com/apisland) |
[Ivan Krasnikov](https://github.com/krivse) |



![](https://img.shields.io/pypi/pyversions/p5?logo=python&logoColor=yellow&style=for-the-badge)
![](https://img.shields.io/badge/Django-2.2.16-blue)
![](https://img.shields.io/badge/DRF-3.12.4-lightblue)
