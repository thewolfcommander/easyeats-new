from django.urls import path

from .views import *


urlpatterns = [
    path('all/', OrderListView.as_view()),
    path('create/', OrderCreateView.as_view()),
    path('update/<int:id>/', OrderUpdateDeleteView.as_view()),
    path('detail/<int:id>/', OrderDetailView.as_view()),
]