from django import forms

from .models import GroceryRequest

class GroceryRequestForm(forms.ModelForm):
    class Meta:
        model = GroceryRequest
        fields = [
            'name',
            'phone_number',
            'info'
        ]