from django import forms

from addresses.models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'address1', 'address2', 'city', 'state', 'country', 'pincode', 'mobile_number', 'alt_mobile']