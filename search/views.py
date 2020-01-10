from rest_framework import generics
from rest_framework import filters

from .serializers import *
from .paginations import *


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class SingerListView(generics.ListAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    pagination_class = AlbumPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = SongPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class AlbumListView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = AlbumPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


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


class AlbumTopView(generics.ListAPIView):
    queryset = Album.objects.all().exclude(rate=None).order_by("-rate")
    serializer_class = AlbumSerializer
    pagination_class = TopPagination
