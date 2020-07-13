from rest_framework import generics, permissions

from .serializers import *
from cart.models import *



class FoodEntryCreateView(generics.CreateAPIView):
    queryset = FoodEntry.objects.all()
    serializer_class = FoodEntrySerializer
    permission_classes = [permissions.AllowAny]


class FoodEntryListView(generics.ListAPIView):
    queryset = FoodEntry.objects.all()
    serializer_class = FoodEntryShowSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = [
        'food',
        'quantity',
        'cost'
    ]

class FoodEntryUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = FoodEntry.objects.all()
    serializer_class = FoodEntrySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    
class FoodEntryDetailView(generics.RetrieveAPIView):
    queryset = FoodEntry.objects.all()
    serializer_class = FoodEntryShowSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'


class GroceryEntryCreateView(generics.CreateAPIView):
    queryset = GroceryEntry.objects.all()
    serializer_class = GroceryEntrySerializer
    permission_classes = [permissions.AllowAny]


class GroceryEntryListView(generics.ListAPIView):
    queryset = GroceryEntry.objects.all()
    serializer_class = GroceryEntryShowSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = [
        'grocery',
        'quantity',
        'cost'
    ]

class GroceryEntryUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = GroceryEntry.objects.all()
    serializer_class = GroceryEntrySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    
class GroceryEntryDetailView(generics.RetrieveAPIView):
    queryset = GroceryEntry.objects.all()
    serializer_class = GroceryEntryShowSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'


class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartShowSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = [
        'user',
        'count',
    ]


class CartCreateView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class CartUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CartDetailView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartShowSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'