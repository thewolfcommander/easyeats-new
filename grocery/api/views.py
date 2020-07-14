from rest_framework import generics, permissions

from .serializers import *
from grocery.models import *
from products.pagination import CustomPageNumberPagination



class GroceryCategoryListView(generics.ListAPIView):
    queryset = GroceryCategory.objects.all()
    serializer_class = GroceryCategoryShowSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = [
        'active'
    ]
    pagination_class = CustomPageNumberPagination


class GroceryCategoryDetailView(generics.RetrieveAPIView):
    queryset = GroceryCategory.objects.all()
    serializer_class = GroceryCategorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'


class GrocerySubCategoryListView(generics.ListAPIView):
    queryset = GrocerySubCategory.objects.all()
    serializer_class = GrocerySubCategoryTinySerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = [
        'active',
        'category',
    ]
    pagination_class = CustomPageNumberPagination


class GrocerySubCategoryDetailView(generics.RetrieveAPIView):
    queryset = GrocerySubCategory.objects.all()
    serializer_class = GrocerySubCategoryTinySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'


class GroceryListView(generics.ListAPIView):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = [
        'grocery_category',
        'active',
        'sub_category',
        'featured'
    ]
    pagination_class = CustomPageNumberPagination



class GroceryDetailView(generics.RetrieveAPIView):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'


class GroceryReviewListView(generics.ListAPIView):
    queryset = GroceryReview.objects.all()
    serializer_class = GroceryReviewSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = [
        'grocery',
        'rating',
        'user'
    ]
    pagination_class = CustomPageNumberPagination


class GroceryReviewCreateView(generics.CreateAPIView):
    queryset = GroceryReview.objects.all()
    serializer_class = GroceryReviewSerializer
    permission_classes = [permissions.IsAuthenticated]



class GroceryRequestCreateView(generics.CreateAPIView):
    queryset = GroceryRequest.objects.all()
    serializer_class = GroceryRequestSerializer
    permission_classes = [permissions.IsAuthenticated]