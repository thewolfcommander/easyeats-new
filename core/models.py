from django.db import models

from accounts.models import User

class Contact(models.Model):
    """
    The information of the users who wants to contact to the administrator will be stored here
    """
    timestamp = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(null=True, blank=True, max_length=255)
    email = models.CharField(null=True, blank=True, max_length=255)
    message = models.TextField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ('-timestamp',)
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    
    def __str__(self):
        return self.full_name

 
class ReportIssue(models.Model):
    """
    The information of the users who wants to report the issues will be stored here
    """
    ISSUE_TYPE = [
        ('technical', 'Having issue in the web application?'),
        ('food', 'Having issue with the food?'),
        ('delivery', 'Having issue with the delivery?'),
        ('other', 'Having some other issue'),
    ]
    timestamp = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(null=True, blank=True, max_length=255)
    email = models.CharField(null=True, blank=True, max_length=255)
    issue_type = models.CharField(max_length=255, choices=ISSUE_TYPE, default='technical')
    message = models.TextField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ('-timestamp',)
        verbose_name = 'Issue and Problem'
        verbose_name_plural = 'Issues and Problems'

    
    def __str__(self):
        return self.full_name

    
class Newsletter(models.Model):
    """
    This model is for newsletter subscription
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.user_id