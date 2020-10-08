from django.urls import path, re_path

from . import login_views
from . import apikey_views

urlpatterns = [
    re_path(r'^login/?', login_views.login, name='login'),
]