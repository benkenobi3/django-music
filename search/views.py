from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response

from django.http import Http404

from .models import *
from .serializers import *


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class SingerListView(generics.ListAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumListView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class GenreDetailView(views.APIView):

    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreDetailSerializer(genre)
        return Response(serializer.data)


class SingerDetailView(views.APIView):

    def get_object(self, pk):
        try:
            return Singer.objects.get(pk=pk)
        except Singer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        singer = self.get_object(pk)
        serializer = SingerDetailSerializer(singer)
        return Response(serializer.data)


class SongDetailView(views.APIView):

    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        song = self.get_object(pk)
        serializer = SongDetailSerializer(song)
        return Response(serializer.data)


class AlbumDetailView(views.APIView):

    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        album = self.get_object(pk)
        serializer = AlbumDetailSerializer(album)
        return Response(serializer.data)
