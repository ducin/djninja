from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djninja.views.home', name='home'),
    # url(r'^djninja/', include('djninja.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', 'articles.views.slider', name='homepage'),
    url(r'^articles/', include('articles.urls')),
    url(r'^lyrics/', include('lyrics.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
