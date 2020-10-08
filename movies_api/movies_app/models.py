from django.db import models

class Movie(models.Model):
    imdb_id = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    overview = models.TextField()


class User(models.Model):
    user_name = models.CharField(max_length=50)
    favourite_movies = models.ManyToManyField(Movie)
