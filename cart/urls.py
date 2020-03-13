from django.urls import path

from cart.views import *

app_name = 'cart'

urlpatterns = [
    path('', cart_home, name='home'),
    path('update/', cart_update, name='update'),
    path('checkout/<int:address_id>/', checkout_home, name='checkout'),
]