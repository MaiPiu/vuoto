from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'giuseppe.views.home', name='home'),
    url(r'^HelloIP/$', 'giuseppe.views.myip', name='home'),
    url(r'^year/$', 'giuseppe.views.year', name='year'),
    url(r'^month/$', 'giuseppe.views.month', name='month'),
    url(r'^day/$', 'giuseppe.views.day', name='day'),
    # url(r'^agostini/', include('agostini.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
