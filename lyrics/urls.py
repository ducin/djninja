from django.conf.urls import patterns, url

from lyrics import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^jukebox$', views.jukebox, name='jukebox'),
    url(r'^(?P<lyric_id>\d+)/$', views.lyric, name='lyric'),
    url(r'^static_about$', views.static_about, name='static_about'),
)
