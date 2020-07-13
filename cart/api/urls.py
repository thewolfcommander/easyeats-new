from django.urls import path

from .views import *

urlpatterns = [
    path('list/', CartListView.as_view()),
    path('create/', CartCreateView.as_view()),
    path('update/<int:id>/', CartUpdateDeleteView.as_view()),
    path('detail/<int:id>/', CartDetailView.as_view()),
    path('food-entry/create/', FoodEntryCreateView.as_view()),
    path('food-entry/all/', FoodEntryListView.as_view()),
    path('food-entry/<int:id>/detail/', FoodEntryDetailView.as_view()),
    path('food-entry/<int:id>/update/', FoodEntryUpdateDeleteView.as_view()),
    path('grocery-entry/create/', GroceryEntryCreateView.as_view()),
    path('grocery-entry/all/', GroceryEntryListView.as_view()),
    path('grocery-entry/<int:id>/detail/', GroceryEntryDetailView.as_view()),
    path('grocery-entry/<int:id>/update/', GroceryEntryUpdateDeleteView.as_view()),
]