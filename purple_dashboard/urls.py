from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'purple_config.views.home', name='home'),
    # url(r'^purple_dashboard/', include('purple_dashboard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/var/www/django/purple_dashboard_root/media/'}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/var/www/django/purple_dashboard_root/static/'}),

)
