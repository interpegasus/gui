from gui.models import *
from users.models import User
from django.contrib import admin
admin.ModelAdmin.list_per_page = 25

class UserAdmin(admin.ModelAdmin):
    #
    fields = ['email']
    #
    list_display = ('id', 'email')
    #
    search_fields = ('id', 'email')

admin.site.register(User,UserAdmin)
