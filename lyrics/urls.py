from django.conf.urls import patterns, url

from lyrics import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<song_id>\d+)/$', views.index, name='song'),
)
