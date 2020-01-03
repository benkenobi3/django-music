from rest_framework import generics

from .serializers import *
from .paginations import *


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class SingerListView(generics.ListAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    pagination_class = AlbumPagination


class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = SongPagination


class AlbumListView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = AlbumPagination


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreDetailSerializer


class SingerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerDetailSerializer


class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongDetailSerializer


class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumDetailSerializer
