from gui.models import *
from django.contrib import admin
admin.ModelAdmin.list_per_page = 25

class ServerAdmin(admin.ModelAdmin):
    #
    fields = ['type']
    #
    list_display = ('id', 'type')
    #
    search_fields = ('id', 'type')

admin.site.register(Server,ServerAdmin)

class HostAdmin(admin.ModelAdmin):
    #
    fields = ['name']
    #
    list_display = ('id', 'name')
    #
    search_fields = ('id', 'name')

admin.site.register(Host,HostAdmin)

class DataCenterAdmin(admin.ModelAdmin):
    #
    fields = ['name']
    #
    list_display = ('id', 'name')
    #
    search_fields = ('id', 'name')

admin.site.register(DataCenter,DataCenterAdmin)

class ClusterAdmin(admin.ModelAdmin):
    #
    fields = ['name']
    #
    list_display = ('id', 'name')
    #
    search_fields = ('id', 'name')

admin.site.register(Cluster,ClusterAdmin)

class ConfigurationAdmin(admin.ModelAdmin):
    #

    #
    search_fields = ('id', 'user')

admin.site.register(Configuration,ConfigurationAdmin)

