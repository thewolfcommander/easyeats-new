from django.urls import path

from . import views

app_name = 'third'

urlpatterns = [
    path('delivery-partner/home/', views.delivery_home, name='delivery_home'),
    path('delivery-partner/deactivate-account/', views.deactivate_profile, name='deactivate_profile'),
    path('delivery-partner/deliveries/new/', views.new_delivery, name='new_delivery'),
    path('delivery-partner/deliveries/shipped/', views.shipped_delivery, name='shipped_delivery'),
    path('delivery-partner/deliveries/delivered/', views.completed_delivery, name='completed_delivery'),
    path('delivery-partner/deliveries/cancelled/', views.cancelled_delivery, name='cancelled_delivery'),
    path('order/update/ship/<int:pk>/', views.ship_delivery, name='ship_delivery'),
    path('order/update/deliver/<int:pk>/', views.complete_delivery, name='complete_delivery'),
    path('order/update/cancel/<int:pk>/', views.cancel_delivery, name='cancel_delivery'),
    path('order/update/assign-delivery-boy/<int:pk>/', views.assign_deliveryboy, name='assign_deliveryboy'),
    path('order/detail/<int:pk>/', views.order_detail, name='order_detail'),
    path('pay/', views.pay, name='pay'),
]