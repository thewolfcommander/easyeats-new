from django.urls import path

from .views import *


urlpatterns = [
    path('restaurants/', RestaurantListView.as_view()),
    path('restaurants/<int:id>/', RestaurantDetailView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:id>/', CategoryDetailView.as_view()),
    path('foods/', FoodListView.as_view()),
    path('foods/<int:id>/', FoodDetailView.as_view()),
    path('foods/reviews/', FoodReviewListView.as_view()),
    path('foods/reviews/create/', FoodReviewCreateView.as_view()),
    path('restaurants/reviews/', RestaurantReviewListView.as_view()),
    path('restaurants/reviews/create/', RestaurantReviewCreateView.as_view()),
]