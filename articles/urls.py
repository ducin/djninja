from django.conf.urls import patterns, url, include

from articles import views

urlpatterns = patterns('',
    url(r'^$', views.slider, name='slider'),
    url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^archive/page/(?P<page>\d+)/$', views.archive, name='archive'),
)
