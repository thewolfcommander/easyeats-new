from django.urls import path

from grocery import views

app_name = 'grocery'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('sub-category/<int:pk>/', views.subcategory_detail, name='subcategory_detail'),
    path('item/<int:pk>/', views.grocery_detail, name='grocery_detail'),
]