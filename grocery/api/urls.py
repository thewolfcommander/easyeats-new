from django.urls import path

from .views import * 


urlpatterns = [
    path('categories/', GroceryCategoryListView.as_view()),
    path('categories/<int:id>/', GroceryCategoryDetailView.as_view()),
    path('sub-categories/', GrocerySubCategoryListView.as_view()),
    path('sub-categories/<int:id>/', GrocerySubCategoryDetailView.as_view()),
    path('items/', GroceryListView.as_view()),
    path('items/<int:id>/', GroceryDetailView.as_view()),
    path('reviews/', GroceryReviewListView.as_view()),
    path('reviews/create/', GroceryReviewCreateView.as_view()),
    path('request/', GroceryRequestCreateView.as_view()),
]