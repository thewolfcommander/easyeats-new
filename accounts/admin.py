from django.contrib import admin

from accounts.models import (
    User,
    Vendor, 
    DeliveryBoy,
)

from core.models import Newsletter

class NewsletterInline(admin.StackedInline):
    model = Newsletter
    extra = 1

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'email', 'mobile_number', 'full_name', 'timestamp']
    inlines = [NewsletterInline]

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['user', 'added', 'business_phone', 'business_email', 'active']
    list_filter = ['added', 'updated', 'active', 'pincode']


@admin.register(DeliveryBoy)
class DeliveryBoyAdmin(admin.ModelAdmin):
    list_display = ['user', 'added', 'business_phone', 'business_email', 'active']
    list_filter = ['added', 'updated', 'active', 'pincode']
    