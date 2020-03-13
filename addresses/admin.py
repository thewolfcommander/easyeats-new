from django.contrib import admin

from addresses.models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'updated']
    list_filter = ['added', 'updated', 'state', 'country', 'pincode']