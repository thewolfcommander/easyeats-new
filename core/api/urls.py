from django.urls import path

from .views import *


urlpatterns = [
    path('contact/', ContactCreateView.as_view()),
    path('newsletter/', NewsletterCreateView.as_view()),
    path('report/', ReportCreateView.as_view()),
]