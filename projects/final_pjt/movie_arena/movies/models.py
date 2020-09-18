from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=200)

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    adult = models.BooleanField()
    overview = models.TextField()
    genre_ids = models.ManyToManyField(Genre, related_name='genre_movie')
    original_language = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200, null=True)
    red = models.IntegerField()
    grey = models.IntegerField()
    yellow = models.IntegerField()
    mint = models.IntegerField()
    skyblue = models.IntegerField()
    dark = models.IntegerField()
    video = models.BooleanField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Rate(models.Model):
    rate = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)