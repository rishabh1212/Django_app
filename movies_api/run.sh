#!/bin/bash
set -ex

cd /movies_api

# Generate schema, at startup keep trying until postgres server is started
until python manage.py makemigrations movies_app
do
  	sleep 3
  	echo "Trying again"
done

# Make tables in postgre
python manage.py migrate

# Populate with required data for testing
./manage.py shell < populate.py

# Run server access on localhost:8000 on docker host
python manage.py runserver 0.0.0.0:8000
