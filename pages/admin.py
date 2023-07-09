from django.contrib import admin
from .models import *

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['user','package','type','price']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['name','lat','long']


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['weight']