from django.urls import path

from cart.views import *

app_name = 'cart'

urlpatterns = [
    path('', cart_home, name='home'),
    path('update/', cart_update, name='update'),
    path('add-to-cart/', add_to_cart, name='add'),
    path('remove-from-cart/', remove_from_cart, name='remove'),
    path('checkout/<int:address_id>/', checkout_home, name='checkout'),
]