from rest_framework import generics

from .models import Genre, Singer, Song, Album
from .serializers import FullGenreSerializer, FullSongSerializer, FullSingerSerializer, FullAlbumSerializer


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = FullGenreSerializer


class SingerListView(generics.ListAPIView):
    queryset = Singer.objects.all()
    serializer_class = FullSingerSerializer


class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = FullSongSerializer


class AlbumListView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = FullAlbumSerializer
