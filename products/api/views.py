from rest_framework import generics, permissions

from .serializers import *
from products.models import *


class RestaurantListView(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [permissions.AllowAny]
    filterset_fields = [
        'name',
        'city',
        'state',
        'country',
        'pincode',
        'active',
        'vendor'
    ]


class RestaurantDetailView(generics.RetrieveAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    filterset_fields = [
        'restaurant',
        'active',
        'name',
    ]


class CategoryListView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'


class FoodListView(generics.ListAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    permission_classes = [permissions.AllowAny]
    filterset_fields = [
        'active',
        'featured',
        'restaurant',
        'category',
    ]


class FoodDetailView(generics.RetrieveAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'


class FoodReviewListView(generics.ListAPIView):
    serializer_class = FoodReviewSerializer
    queryset = FoodReview.objects.all()
    permission_classes = [permissions.AllowAny]
    filterset_fields = [
        'food',
        'rating_1',
        'user',
    ]


class FoodReviewCreateView(generics.CreateAPIView):
    serializer_class = FoodReviewSerializer
    queryset = FoodReview.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class RestaurantReviewListView(generics.ListAPIView):
    serializer_class = RestaurantReviewSerializer
    queryset = RestaurantReview.objects.all()
    permission_classes = [permissions.AllowAny]
    filterset_fields = [
        'restaurant',
        'rating_1',
        'user',
    ]


class RestaurantReviewCreateView(generics.CreateAPIView):
    serializer_class = RestaurantReviewSerializer
    queryset = RestaurantReview.objects.all()
    permission_classes = [permissions.IsAuthenticated]