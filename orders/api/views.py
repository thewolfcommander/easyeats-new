from rest_framework import generics, permissions

from orders.models import *
from .serializers import *


class OrderListView(generics.ListAPIView):
    serializer_class = OrderShowSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields =[
        'order_id',
        'user',
        'delivery_boy',
        'address',
        'status',
        'active'
    ]


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class OrderUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderShowSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'