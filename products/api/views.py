from rest_framework import generics, permissions

from .serializers import *
from products.models import *
from products.pagination import CustomPageNumberPagination


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
    pagination_class = CustomPageNumberPagination


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
    pagination_class = CustomPageNumberPagination


class CategoryDetailView(generics.RetrieveAPIView):
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
    pagination_class = CustomPageNumberPagination


class FoodDetailView(generics.RetrieveAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'


class FoodReviewListView(generics.ListAPIView):
    serializer_class = FoodReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [permissions.AllowAny]
    filterset_fields = [
        'food',
        'rating_1',
        'user',
    ]
    pagination_class = CustomPageNumberPagination


class FoodReviewCreateView(generics.CreateAPIView):
    serializer_class = FoodReviewSerializer
    queryset = Review.objects.all()
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
    pagination_class = CustomPageNumberPagination


class RestaurantReviewCreateView(generics.CreateAPIView):
    serializer_class = RestaurantReviewSerializer
    queryset = RestaurantReview.objects.all()
    permission_classes = [permissions.IsAuthenticated]