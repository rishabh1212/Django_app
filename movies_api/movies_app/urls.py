from django.urls import path, re_path

from . import login_views
from . import apikey_views

urlpatterns = [
    re_path(r'^favorites$', login_views.favorites, name='favorites'),
    re_path(r'^favorite/(?P<imdb_id>\w+)$', login_views.favorite, name='index'),
    re_path(r'^login/?', login_views.login, name='login'),
]