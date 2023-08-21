!/usr/bin/bash
# exit on error
# set -o errexit


apt update -y && apt upgrade -y && apt install -y --no-install-recommends binutils libproj-dev gdal-bin libgdal-dev python3-gdal


# pip install --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==`gdal-config --version`


# pip install -r requirements.txt
# python manage.py collectstatic --no-input

# python manage.py makemigrations core
# python manage.py migrate core

# python manage.py makemigrations users
# python manage.py migrate users

# python manage.py makemigrations seekers
# python manage.py migrate seekers

# python manage.py makemigrations employers
# python manage.py migrate employers

# python manage.py makemigrations
# python manage.py migrate

