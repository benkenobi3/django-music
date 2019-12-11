from django.conf.urls import url, include

from .views import GenreListView, SingerListView, SongListView, AlbumListView


urlpatterns = [
    url(r'^genre/all/$', GenreListView.as_view()),
    url(r'^singer/all/$', SingerListView.as_view()),
    url(r'^song/all/$', SongListView.as_view()),
    url(r'^album/all/$', AlbumListView.as_view()),
]