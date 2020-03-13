from django.contrib import admin

from core.models import (
    Contact,
    ReportIssue
)

admin.site.site_header = "EasyEats Admin - Powered by RIGHTBROS"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'timestamp', 'ip_address']
    list_filter = ['timestamp']


@admin.register(ReportIssue)
class ReportIssueAdmin(admin.ModelAdmin):
    list_display = ['issue_type', 'is_resolved', 'full_name', 'email', 'timestamp', 'ip_address']
    list_filter = ['issue_type', 'is_resolved', 'timestamp']