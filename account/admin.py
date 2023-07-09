from django.contrib import admin
from .models import *
from django.utils.html import format_html

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone_no']

# Register your models here.
@admin.register(DriverInfo)
class DriverInfoAdmin(admin.ModelAdmin):
    list_display =['display_avatar','user']
    list_select_related = ['user']


    def display_avatar(self,obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.avatar.url))
    display_avatar.allow_tages=True
    display_avatar.short_description='avatar'