# 概要

app 内はアプリ用のサンプル
それ以外はプロジェクト用のサンプル

## セットアップ

- pipenv --python 3.9
- pipenv install hoge...
- pip freeze > requirements.txt
- docker-compose up --build
- docker-compose exec app bash
- cd workdir
- django-admin startproject project .
- python manage.py startapp app
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver 0.0.0.0:8000

### /.env

SECRET_KEY
DEBUG

DB_NAME
DB_USER
DB_HOST

CLOUDINARY_API_SECRET

EMAIL_HOST
EMAIL_HOST_USER
EMAIL_HOST_PASSWOR=
EMAIL_PORT

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET

#### sample

DB_NAME=postgres
DB_USER=postgres
DB_HOST=db

CLOUDINARY_API_SECRET=

EMAIL_HOST=smtp.sendgrid.net
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=587

## デプロイ（Heroku）

- heroku config:push
  ...
- git push heroku master
- heroku run python3 manage.py migrate
- heroku run python3 manage.py createsuperuser
