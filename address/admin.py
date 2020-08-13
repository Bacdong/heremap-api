from django.contrib import admin
from .models import Address
from .models import APIKey

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartment_number', 
                    'street', 'ward', 'district', 'city', )

    list_filter = ('ward', 'district', 'city', ) 
    search_fields = ['id', 'apartment_number', 
                    'street', 'ward', 'district', 'city', ]


class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'status')
    list_filter = ('id', 'key', 'status')
    search_fields = ['id', 'key', 'status']



admin.site.register(Address, AddressAdmin)
admin.site.register(APIKey, APIKeyAdmin)
