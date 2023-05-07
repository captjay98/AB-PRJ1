#!/usr/bin/env bash
# exit on error
set -o errexit


pip install -r requirements.txt
python manage.py collectstatic --no-input

python manage.py makemigrations core
python manage.py migrate core

python manage.py makemigrations users
python manage.py migrate users

python manage.py makemigrations seekers
python manage.py migrate seekers

python manage.py makemigrations employers
python manage.py migrate employers

python manage.py makemigrations
python manage.py migrate
