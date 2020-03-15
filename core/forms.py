from django import forms

from core.models import (
    Contact, 
    ReportIssue,
    Newsletter,
    HotelReservation
)

class ContactForm(forms.ModelForm):
    """
    This form will get all the information related to the contact
    """
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']


class ReportIssueForm(forms.ModelForm):
    """
    This form will recieve information about the issues experienced by Users
    """
    class Meta:
        model = ReportIssue
        fields = ['issue_type', 'full_name', 'email', 'message']

    
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']

    
class HotelReservationForm(forms.ModelForm):
    class Meta:
        model = HotelReservation
        fields = ['full_name', 'restaurant', 'email', 'mobile_number', 'people']