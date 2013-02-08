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
    url(r'^$', 'gui.views.front_page'),
    url(r'^/$','gui.views.front_page'),
    url(r'^configuration_form/','gui.views.configuration_form'),
    # User Session
    url(r'^enter/', 'users.views.enter'),
    url(r'^exit/', 'users.views.exit_request'),
    url(r'^forgot_password/', 'users.views.forgot_password'),
    url(r'^process_sign_up/', 'users.views.process_sign_up'),
    url(r'^process_create_account/', 'users.views.process_create_account'),
    url(r'^process_forgot_password/', 'users.views.process_forgot_password'),
)

handler404 = 'gui.views.my_custom_404_view'
handler500 = 'gui.views.my_custom_500_view'