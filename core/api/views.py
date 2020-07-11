from rest_framework import generics, permissions

from core.models import *
from .serializers import *


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]


class ReportCreateView(generics.CreateAPIView):
    queryset = ReportIssue.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.AllowAny]


class NewsletterCreateView(generics.CreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [permissions.AllowAny]