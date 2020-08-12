from django.contrib import admin
from .models import Address

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'apartment_number', 'street', 'ward', 'district', 'city',
    )

    list_filter = ('ward', 'district', 'city', ) 

    search_fields = [
        'id', 'apartment_number', 'street', 'ward', 'district', 'city',
    ]


admin.site.register(Address, AddressAdmin)