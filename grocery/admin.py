from django.contrib import admin

from .models import Grocery, GroceryCategory, GroceryImage, GroceryReview, GroceryTag, GrocerySubCategory

class GroceryImageInline(admin.TabularInline):
    model = GroceryImage
    extra = 1


class GroceryTagInline(admin.TabularInline):
    model = GroceryTag
    extra = 1

class GroceryReviewInline(admin.TabularInline):
    model = GroceryReview
    extra = 0


class GrocerySubCategoryInline(admin.TabularInline):
    model = GrocerySubCategory
    extra = 1


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
    inlines = [GrocerySubCategoryInline]


@admin.register(GrocerySubCategory)
class GrocerySubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'updated', 'category']
    list_filter = ['active', 'added', 'updated']
    search_fields = ['name',]