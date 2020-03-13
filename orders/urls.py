from django.urls import path

from .views import create_order, order_success, order_failed

app_name = 'orders'

urlpatterns = [
    path('create/', create_order, name='create'),
    path('success/', order_success, name='success'),
    path('failed/', order_failed, name='failed'),
]