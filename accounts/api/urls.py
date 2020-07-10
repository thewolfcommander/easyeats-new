from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

urlpatterns = [
    path('login/', obtain_auth_token),
    path('register/', UserCreateAPIView.as_view()),
    path('users/', UserListAPIView.as_view()),
    path('users/<slug:user_id>/', UserDetailAPIView.as_view()),
    path('vendors/', VendorListAPIView.as_view()),
    path('vendors/create/', VendorCreateAPIView.as_view()),
    path('vendors/<int:id>/', VendorDetailAPIView.as_view()),
    path('dboys/', DeliveryBoyListAPIView.as_view()),
    path('dboys/create/', DeliveryBoyCreateAPIView.as_view()),
    path('dboys/<int:id>/', DeliveryBoyDetailAPIView.as_view()),
]