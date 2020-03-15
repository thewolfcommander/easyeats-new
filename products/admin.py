from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from products.models import *

class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImage
    extra = 1


class FoodImageInline(admin.TabularInline):
    model = FoodImage
    extra = 1

class FoodTagInline(admin.TabularInline):
    model = FoodTag
    extra = 1


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Restaurant)
class RestaurantAdmin(ImportExportModelAdmin):
    list_display = ['name', 'mobile_number', 'email', 'vendor', 'added', 'active']
    list_filter = ['added', 'updated', 'pincode']
    inlines = [RestaurantImageInline]


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'active', 'added']
    list_filter = ['active', 'added', 'updated']


@admin.register(Food)
class FoodAdmin(ImportExportModelAdmin):
    list_display = ['name', 'active', 'added', 'gross_price', 'discount_price', 'added_by']
    list_filter = ['active', 'added', 'updated']
    inlines = [FoodImageInline, FoodTagInline, ReviewInline]


@admin.register(Collection)
class CollectionAdmin(ImportExportModelAdmin):
    list_display = ['name', 'active', 'added']
    list_filter = ['active', 'added', 'updated']