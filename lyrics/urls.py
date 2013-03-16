from django.conf.urls import patterns, url

from lyrics import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^jukebox$', views.jukebox, name='jukebox'),
    url(r'^(?P<song_id>\d+)/$', views.song, name='song'),
    url(r'^static_about$', views.static_about, name='static_about'),
)
