from django.urls import path

from . import views

app_name = 'third'

urlpatterns = [
    path('vendor/home/', views.vendor_home, name='vendor_home'),
    path('vendor/restaurants/', views.vendor_restaurants, name='vendor_restaurants'),
    path('vendor/restaurants/<int:pk>/', views.vendor_restaurant_detail, name='vendor_restaurant_detail'),
]