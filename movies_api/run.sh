#!/bin/bash
set -ex

cd /movies_app/movies_api

# python manage.py makemigrations
until python manage.py makemigrations movies_app
do
  	sleep 3
  	echo "Trying again"
done
if  python manage.py check; then
python manage.py migrate
fi

cd /app
until python populate.py 
do 
	sleep 3
done

cd /movies_app/movies_api
python manage.py runserver
