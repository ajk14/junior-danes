from django.conf.urls import patterns, include, url
import os
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'danes.views.home'),
                       url(r'^winter/$', 'danes.views.winter'),
                       url(r'^summer/$', 'danes.views.summer'),
                       url(r'^showcases/$', 'danes.views.showcases'),
                       url(r'^register/$', 'danes.views.register'),
                       url(r'^showcases/register/$', 'danes.views.showregister'),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': os.path.join(SITE_ROOT, 'static')}),
    # Examples:
    # url(r'^$', 'danes.views.home', name='home'),
    # url(r'^danes/', include('danes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
                           url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
                           url(r'^admin/', include(admin.site.urls)),
)
