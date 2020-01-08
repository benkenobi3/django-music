from django.db import models


class Genre(models.Model):

    name = models.CharField(max_length=200)


class Singer(models.Model):

    name = models.CharField(max_length=200)
    poster_url = models.CharField(max_length=200, default="")
    avatar_url = models.CharField(max_length=200, default="")


class Song(models.Model):

    name = models.CharField(max_length=200)
    duration = models.TimeField()

    img_url = models.CharField(max_length=200, default="")

    singers = models.ManyToManyField(Singer, related_name="songs")
    genres = models.ManyToManyField(Genre, related_name="songs")


class Album(models.Model):

    name = models.CharField(max_length=200)
    duration = models.TimeField()
    type = models.CharField(max_length=200)
    date = models.DateField()
    rate = models.IntegerField(null=True)

    img_url = models.CharField(max_length=200, default="")

    singers = models.ManyToManyField(Singer, related_name="albums")
    songs = models.ManyToManyField(Song, related_name="albums")
    genres = models.ManyToManyField(Genre, related_name="albums")
