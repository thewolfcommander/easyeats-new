from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_id", "user", "timestamp", "updated", "total", "status"]
    list_filter = ["timestamp", "updated", "status"]