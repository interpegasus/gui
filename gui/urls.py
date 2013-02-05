from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Configuration Form
    url(r'^$', 'ui.views.views.home_list_options'),
    url(r'^/$','ui.views.views.home_list_options'),
    url(r'^/$','ui.views.views.home_list_options'),
    url(r'^/$','ui.views.views.configuration_form'),

    # User Session
    url(r'^enter/', 'ui.views.enter'),
    url(r'^exit/', 'ui.views.exit_request'),
    url(r'^forgot_password/', 'ui.views.forgot_password'),
    url(r'^process_sign_up/', 'ui.views.process_sign_up'),
    url(r'^process_create_account/', 'ui.views.process_create_account'),
    url(r'^process_forgot_password/', 'ui.views.process_forgot_password'),
)

handler404 = 'ui.views.my_custom_404_view'
handler500 = 'ui.views.my_custom_500_view'