from rest_framework import generics, permissions

from .serializers import *
from .permissions import *
from accounts.models import *


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserShowSerializer
    queryset = User.objects.all()
    filterset_fields = [
        'gender',
        'mobile_number',
        'order_count',
        'is_client',
        'is_vendor',
        'is_delivery',
        'is_newsletter',
        'is_admin'
    ]
    permission_classes = [permissions.IsAuthenticated]


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserShowSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'user_id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class VendorListAPIView(generics.ListAPIView):
    serializer_class = VendorShowSerializer
    queryset = Vendor.objects.all()
    filterset_fields = [
        'user',
        'city',
        'state',
        'country',
        'pincode',
        'active'
    ]
    permission_classes = [permissions.IsAuthenticated]


class VendorCreateAPIView(generics.CreateAPIView):
    serializer_class = VendorCreateSerializer
    queryset = Vendor.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class VendorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VendorShowSerializer
    queryset = Vendor.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnlyVendor]
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)



class DeliveryBoyListAPIView(generics.ListAPIView):
    serializer_class = DeliveryBoyShowSerializer
    queryset = DeliveryBoy.objects.all()
    filterset_fields = [
        'user',
        'city',
        'state',
        'country',
        'pincode',
        'active'
    ]
    permission_classes = [permissions.IsAuthenticated]


class DeliveryBoyCreateAPIView(generics.CreateAPIView):
    serializer_class = DeliveryBoyCreateSerializer
    queryset = DeliveryBoy.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class DeliveryBoyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeliveryBoyShowSerializer
    queryset = DeliveryBoy.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnlyDBoy]
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)