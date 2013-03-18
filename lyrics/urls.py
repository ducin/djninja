from django.conf.urls import patterns, url, include
#from django.contrib import auth

from lyrics import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^jukebox$', views.jukebox, name='jukebox'),
    url(r'^(?P<lyric_id>\d+)/$', views.lyric, name='lyric'),
    url(r'^static_about$', views.static_about, name='static_about'),
    url(r'^login$', views.login, name='login'),
    url(r'^login_process$', views.login_process, name='login_process'),
#    url(r'^logout$', auth.logout, {'next_page': '/successfully_logged_out/'}),
    (r'', include('django.contrib.auth.urls')),
)
