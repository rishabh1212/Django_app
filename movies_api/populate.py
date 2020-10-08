"""
dump movies database
"""
import pandas as pd
import os
from sqlalchemy import create_engine

engine = create_engine(
	'postgresql://{}:{}@{}:{}/{}'.format(
		os.environ.get('POSTGRES_USER'),
		os.environ.get('POSTGRES_PASSWORD'),
		os.environ.get('POSTGRES_HOST'),
		os.environ.get('POSTGRES_PORT'),
		os.environ.get('POSTGRES_DB')
	)
)
pd.read_csv('movies.csv')[
	['imdb_id', 'original_title', 'overview']
].dropna().drop_duplicates(subset=['imdb_id']).to_sql(
	'movies_app_movie', con=engine, if_exists="append", index=False
)

"""
create super user to see/share apikeys
"""
print("BELOW VALUES ARE ONLY PRINTED FOR EASE OF TESTING")
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')

print('================ADMIN======================')
print('admin===> user_id: admin')
print('admin===> password: adminpass')
print('admin===> email: admin@example.com')
print('===========================================')

"""
create api keys which only super user can see
"""
from rest_framework_api_key.models import APIKey
api_key, key = APIKey.objects.create_key(name="movies_read_apikey")

print('================APIKEY=====================')
print('key===>', key)
print('===========================================')

"""
create a test user ris:pas and add one favorite movie
"""
from movies_app.models import *
u = User(username='ris', is_active=True)
u.set_password('pas')
u.save()
userfavorites(user=User.objects.get(username='ris')).save()
userfavorites.objects.get(user__username='ris').favorite_movies.add(movie.objects.first())

print('================TestUser===================')
print('testuser===> user_id: ris')
print('testuser===> password: pas')
print('===========================================')
