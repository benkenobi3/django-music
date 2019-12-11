from django.db import models


class Genre(models.Model):

    name = models.CharField(max_length=200)


class Singer(models.Model):

    name = models.CharField(max_length=200)


class Song(models.Model):

    name = models.CharField(max_length=200)
    duration = models.TimeField()

    singers = models.ManyToManyField(Singer)
    genres = models.ManyToManyField(Genre)


class Album(models.Model):

    name = models.CharField(max_length=200)
    duration = models.TimeField()
    type = models.CharField(max_length=200)
    date = models.DateField()
    rate = models.IntegerField(null=True)

    singers = models.ManyToManyField(Singer)
    songs = models.ManyToManyField(Song)
    genres = models.ManyToManyField(Genre)
