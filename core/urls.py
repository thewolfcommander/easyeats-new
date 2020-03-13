from django.urls import path

from core.views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('partner-relations/', partner_relations, name='partner_relations'),
    path('terms-of-service/', terms_of_service, name='terms_of_service'),
    path('join-as-vendor/', join_as_vendor, name='join_as_vendor'),
    path('join-as-delivery-boy/', join_as_delivery_boy, name='join_as_delivery_boy'),
    path('report-issue/', report, name='report'),
]