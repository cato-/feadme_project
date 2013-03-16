from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('feedjack.urls'), name='home'),

    url(r'^accounts/', include('feadme.registration_urls')),
    #url(r'^accounts/$', include('django.contrib.auth.urls'), name='accounts'),

    # url(r'^feadme_project/', include('feadme_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('feedjack.urls'), name='home'),
)
