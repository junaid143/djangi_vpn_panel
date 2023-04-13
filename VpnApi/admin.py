from django.contrib import admin
from .models import VpnModel


# Register your models here.

@admin.register(VpnModel)
class VpnAdmin(admin.ModelAdmin):
    list_display = ['id' , 'hostname' , 'countryshort' , 'username' ,'config' , 'is_enable']
    # readonly_fields =['hostname']
