from rest_framework import serializers
from .models import Genre, Song, Singer, Album


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name',)


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ('id', 'name', 'avatar_url',)


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'name', 'img_url', 'duration',)


class AlbumSerializer(serializers.ModelSerializer):

    singers = SingerSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'name', 'img_url', 'duration', 'type', 'date', 'rate', 'singers',)


class GenreDetailSerializer(serializers.ModelSerializer):

    songs = SongSerializer(many=True, read_only=True)
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Singer
        fields = ('id', 'name', 'songs', 'albums')


class SingerDetailSerializer(serializers.ModelSerializer):

    songs = SongSerializer(many=True, read_only=True)
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Singer
        fields = ('id', 'name', 'avatar_url', 'poster_url', 'songs', 'albums',)


class SongDetailSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True, read_only=True)
    singers = SingerSerializer(many=True, read_only=True)
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Song
        fields = ('id', 'name', 'img_url', 'duration', 'genres', 'singers', 'albums',)


class AlbumDetailSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True, read_only=True)
    singers = SingerSerializer(many=True, read_only=True)
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'name', 'img_url', 'duration', 'type', 'date', 'rate', 'genres', 'singers', 'songs',)
