from django.db import models
from django.contrib.auth.models import User


class movie(models.Model):
    """
    Movie table
    """
    imdb_id = models.CharField(max_length=200, primary_key=True)
    original_title = models.CharField(max_length=200)
    overview = models.TextField()

class userfavorites(models.Model):
    """
    Define relationship between users and movies
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    favorite_movies = models.ManyToManyField(movie)
