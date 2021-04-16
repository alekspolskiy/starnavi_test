# Starnavi test work
This project is simple REST API to user signup and user login and authentication with JWT tokens, 
post create, like and unlike, and likes analytics also.
## How to install
Recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html)
or [conda env](https://conda.io/projects/conda/en/latest/index.html).
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
After requirements was successfully installed use [docker-compose](https://docs.docker.com/):
```
docker-compose up
```
Run makemigrations:
```
python manage.py makemigrations
```
And migrate:
```
python manage.py migrate
```
For run server:
```
python manage.py runserver
```
## API
First you need is signup.
### Signup
POST: /api/v1/signup/
#### Request Example:
```
curl -v -X POST \
-d '{
        "username": "username",
        "email": "example@gmail.com",
        "password": "password"
    }
}' "localhost:8000/api/v1/signup/"
```
#### Response Example:
```
{
    "email": "example@gmail.com",
    "username": "username"
}
```
User was successfully created.
### Login
POST: /api/v1/login/
#### Request Example:
```
curl -v -X POST \
-d '{
        "username": "username",
        "password": "password"
    }
}' "localhost:8000/api/v1/login/"
```
#### Response Example:
```
{
    "username": "username",
    "token": {
        "refresh": "refresh_token",
        "access": "access_token"
    }
}
```
Access token has expired time 60 minutes. To refresh token use:
### Refresh token
POST: /api/v1/token/refresh/
#### Request Example:
```
curl -v -X POST \
-d '{
        "refresh": "refresh_token",
    }
}' "localhost:8000/api/v1/token/refresh/"
```
#### Response Example:
```
{
    "access": "access_token"
}
```
Now you can create posts.
### Post create
POST: /api/v1/posts/create/
#### Request Example:
```
curl -v -X POST \
-H "Authorization: Bearer {access_token}" \
-d '{
        "title": "Post1",
        "content": "content",
    }
}' "localhost:8000/api/v1/posts/create/"
```
#### Response Example:
```
{
    "id": 1,
    "title": "Post1",
    "author": "username",
    "content": "content",
    "email": "example@gmail.com",
    "date": "2021-04-15T04:11:40.539764Z"
}
```
### Get posts
GET: /api/v1/posts/
#### Request Example:
```
curl -v -X GET \
-H "Authorization: Bearer {access_token}" \
"localhost:8000/api/v1/posts/"
```
#### Response Example:
```
[
    {
        "id": 1,
        "title": "Post1",
        "author": "username",
        "content": "content",
        "email": "example@gmail.com",
        "date": "2021-04-15T00:08:26.610313Z",
        "like": 0,
        "unlike": 0
    },
    {
        "id": 2,
        "title": "Post2",
        "author": "username",
        "content": "content",
        "email": "example@gmail.com",
        "date": "2021-04-15T04:01:45.339196Z",
        "like": 0,
        "unlike": 0
    }
]
```
### Get post
GET: /api/v1/post/{post_id}/
#### Request Example:
```
curl -v -X GET \
-H "Authorization: Bearer {access_token}" \
"localhost:8000/api/v1/posts/{post_id}/"
```
#### Response Example:
```
[
    {
        "id": 1,
        "title": "Post1",
        "author": "username",
        "content": "content",
        "email": "example@gmail.com",
        "date": "2021-04-15T00:08:26.610313Z",
        "like": 0,
        "unlike": 0
    }
]
```
### Post like
POST: api/v1/posts/{post_id}/like/
#### Request Example:
```
curl -v -X POST \
-H "Authorization: Bearer {access_token}" \
}' "localhost:8000/api/v1/posts/{post_id}/like/"
```
#### Response Example:
```
{
    "id": 1,
    "date": "2021-04-15T00:08:47.462843Z",
    "user": 1,
    "post": 1
}
```
The same to unlike posts.
### Post unlike
POST: api/v1/posts/{post_id}/unlike/
#### Request Example:
```
curl -v -X POST \
-H "Authorization: Bearer {access_token}" \
}' "localhost:8000/api/v1/posts/{post_id}/unlike/"
```
#### Response Example:
```
{
    "id": 1,
    "user": 1,
    "post": 1
}
```
### Get users
GET: /api/v1/users/
#### Request Example:
```
curl -v -X GET \
-H "Authorization: Bearer {access_token}" \
"localhost:8000/api/v1/users/"
```
#### Response Example:
```
[
    {
        "id": 1,
        "password": "password",
        "last_login": "2021-04-15T04:01:13.207579Z",
        "is_superuser": false,
        "first_name": "",
        "last_name": "",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-04-15T00:07:32.656221Z",
        "username": "username",
        "email": "example@gmail.com",
        "created_at": "2021-04-15T00:07:32.736028Z",
        "last_request": "2021-04-15T04:31:29.855358Z",
        "groups": [],
        "user_permissions": []
    },
    {
        "id": 2,
        "password": "password",
        "last_login": "2021-04-15T04:04:13.207579Z",
        "is_superuser": false,
        "first_name": "",
        "last_name": "",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-04-15T00:03:32.656221Z",
        "username": "username2",
        "email": "example2@gmail.com",
        "created_at": "2021-04-15T00:03:32.736028Z",
        "last_request": "2021-04-15T04:30:29.855358Z",
        "groups": [],
        "user_permissions": []
    }
]
```
### Get user
GET: /api/v1/users/{user_id}/
#### Request Example:
```
curl -v -X GET \
-H "Authorization: Bearer {access_token}" \
"localhost:8000/api/v1/users/{user_id}/"
```
#### Response Example:
```
[
    {
        "id": 1,
        "password": "password",
        "last_login": "2021-04-15T04:01:13.207579Z",
        "is_superuser": false,
        "first_name": "",
        "last_name": "",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-04-15T00:07:32.656221Z",
        "username": "username",
        "email": "example@gmail.com",
        "created_at": "2021-04-15T00:07:32.736028Z",
        "last_request": "2021-04-15T04:31:29.855358Z",
        "groups": [],
        "user_permissions": []
    }
]
```
### Get analytics
GET: /api/v1/analytics/
#### Request parameters:
date_from - day from which the counting of likes starts (requiered) \
date_to - day to which the counting ends, include this day (requiered)
#### Request Example:
```
curl -v -X GET \
-H "Authorization: Bearer {access_token}" \
"localhost:8000/api/v1/analytics/?date_from=2021-4-11&date_to=2021-4-14"
```
#### Response Example:
```
{
    "2021-04-11": 2,
    "2021-04-12": 5,
    "2021-04-13": 0,
    "2021-04-14": 1
}
```