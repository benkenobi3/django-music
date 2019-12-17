from django.conf.urls import url, include

from .views import *

urlpatterns = [
    url(r'^genre/all/$', GenreListView.as_view()),
    url(r'^genre/(?P<pk>\d+)/$', GenreDetailView.as_view()),
    url(r'^singer/all/$', SingerListView.as_view()),
    url(r'^singer/(?P<pk>\d+)/$', SingerDetailView.as_view()),
    url(r'^song/all/$', SongListView.as_view()),
    url(r'^song/(?P<pk>\d+)/$', SongDetailView.as_view()),
    url(r'^album/all/$', AlbumListView.as_view()),
    url(r'^album/(?P<pk>\d+)/$', AlbumDetailView.as_view()),
]
