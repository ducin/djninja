from django.conf.urls import patterns, url, include
#from django.contrib import auth

from lyrics import views

urlpatterns = patterns('',
    url(r'^jukebox$', views.jukebox, name='jukebox'),
    url(r'^(?P<lyric_id>\d+)/$', views.lyric, name='lyric'),
    url(r'^static_about$', views.static_about, name='static_about'),
#    url(r'^logout$', auth.logout, {'next_page': '/successfully_logged_out/'}),
    (r'', include('django.contrib.auth.urls')),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/successfully_logged_out/'})
#    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
