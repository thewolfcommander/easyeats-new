from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import (
    User, 
    Vendor,
    DeliveryBoy
)


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('user_id', 'email', 'mobile_number', 'full_name', 'password1', 'password2')

    
class UserDetailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ( 'profile_photo', 'user_id', 'email', 'mobile_number', 'full_name', 'gender')

    
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['business_phone', 'business_email', 'address1', 'address2', 'city', 'landmark', 'state', 'country', 'pincode']

    
class DeliveryBoyForm(forms.ModelForm):
    class Meta:
        model = DeliveryBoy
        fields = ['business_phone', 'business_email', 'address1', 'address2', 'city', 'landmark', 'state', 'country', 'pincode']