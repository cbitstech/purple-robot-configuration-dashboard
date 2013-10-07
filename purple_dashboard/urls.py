from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^home', 'purple_config.views.home', name='home'),
     url(r'^save_config', 'purple_config.views.save_config', name='save_config'),
     url(r'^get_config', 'purple_config.views.get_config', name='get_config'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/var/www/django/purple_dashboard_root/media/'}),

)
