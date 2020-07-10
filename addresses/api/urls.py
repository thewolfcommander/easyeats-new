from django.urls import path

from .views import *

urlpatterns = [
    path('addresses/', ListCreateAddressAPIVIew.as_view()),
    path('addresses/<int:id>/', DetailAddressAPIVIew.as_view()),
]