from django.urls import path
from addresses.views import add_address, select_address

app_name = 'addresses'

urlpatterns = [
    path('', select_address, name='select'),
    path('add/', add_address, name='add'),
]