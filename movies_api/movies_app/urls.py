from django.urls import path, re_path

# For APIs which require login sessions
from . import login_views
# For APIs which require API Key
from . import apikey_views

urlpatterns = [
    re_path(r'^movies$', apikey_views.filter_movies, name='movies'),
    re_path(r'^movie/(?P<imdb_id>\w+)$', apikey_views.describe_movie, name='movie'),
    re_path(r'^favorites$', login_views.favorites, name='favorites'),
    re_path(r'^favorite/(?P<imdb_id>\w+)$', login_views.favorite, name='favorite'),
    re_path(r'^login/?', login_views.login, name='login'),
]