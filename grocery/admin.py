from django.contrib import admin

from .models import Grocery, GroceryCategory, GroceryImage, GroceryReview, GroceryTag

class GroceryImageInline(admin.TabularInline):
    model = GroceryImage
    extra = 1


class GroceryTagInline(admin.TabularInline):
    model = GroceryTag
    extra = 1

class GroceryReviewInline(admin.TabularInline):
    model = GroceryReview
    extra = 0


@admin.register(Grocery)
class GroceryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'updated', 'gross_price', 'discount_price', 'featured']
    list_editable = ['featured',]
    list_filter = ['active', 'added', 'updated', 'featured']
    search_fields = ['name', 'summary']
    inlines = [GroceryImageInline, GroceryTagInline, GroceryReviewInline]


@admin.register(GroceryCategory)
class GroceryCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'updated']
    list_filter = ['active', 'added', 'updated']
    search_fields = ['name',]