from django.urls import path

from products.views import *

app_name = 'products'

urlpatterns = [
    path('menu/', menu, name='menu'),
    path('menu/food/<int:pk>/', food_detail, name='food_detail'),
    path('restaurants/', restaurant_list, name='restaurants'),
    path('restaurants/<int:pk>/', restaurant_detail, name='restaurant_detail'),
    path('categories/', categories_list, name="categories"),
    path('categories/<int:pk>/', categories_detail, name="categories_detail"),
    path('collections/', collection_list, name="collections"),
    path('collections/<int:pk>/', collection_detail, name="collections_detail"),
]