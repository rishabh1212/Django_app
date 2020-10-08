#!/bin/bash
set -ex

cd /movies_api

# python manage.py makemigrations
until python manage.py makemigrations movies_app
do
  	sleep 3
  	echo "Trying again"
done

python manage.py migrate

./manage.py shell < populate.py

python manage.py runserver 0.0.0.0:8000
