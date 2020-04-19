from django.urls import path

from grocery import views

app_name = 'grocery'

urlpatterns = [
    path('', views.home, name='home'),
]