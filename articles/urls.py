from django.conf.urls import patterns, url, include

from articles import views

urlpatterns = patterns('',
    url(r'^$', views.slider, name='slider'),
)
