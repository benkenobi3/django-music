from django.conf.urls import url, include

from django.urls import path

from .views import *

urlpatterns = [
    path('genre/all/', GenreListView.as_view()),
    path('genre/<int:pk>/', GenreDetailView.as_view()),
    path('singer/all/', SingerListView.as_view()),
    path('singer/<int:pk>/', SingerDetailView.as_view()),
    path('song/all/', SongListView.as_view()),
    path('song/<int:pk>/', SongDetailView.as_view()),
    path('album/all/', AlbumListView.as_view()),
    path('album/<int:pk>/', AlbumDetailView.as_view()),
]
