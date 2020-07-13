from rest_framework import serializers

from addresses.models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'user',
            'address1',
            'address2',
            'city',
            'state',
            'country',
            'pincode',
            'mobile_number',
            'alt_mobile',
            'added',
            'updated'
        )