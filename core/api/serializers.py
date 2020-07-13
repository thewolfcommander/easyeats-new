from rest_framework import serializers

from core.models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'timestamp',
            'full_name',
            'message',
            'ip_address',
            'email'
        ]


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportIssue
        fields = [
            'id',
            'timestamp',
            'full_name',
            'message',
            'ip_address',
            'email',
            'issue_type',
            'is_resolved'
        ]


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = [
            'id',
            'user',
            'email',
            'active',
            'added'
        ]