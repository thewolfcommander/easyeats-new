from rest_framework import generics, permissions

from .serializers import AddressSerializer
from addresses.models import Address

from .permissions import *


class ListCreateAddressAPIVIew(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    filterset_fields = [
        'user',
        'city',
        'state',
        'country',
        'pincode',
        'mobile_number',
    ]
    permission_classes = [permissions.IsAuthenticated]



class DetailAddressAPIVIew(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)