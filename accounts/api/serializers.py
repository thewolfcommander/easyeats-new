from rest_framework import serializers


from accounts.models import *


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'user_id',
            'full_name',
            'email',
            'password',
            'is_client',
            'is_vendor',
            'is_delivery',
            'is_newsletter'
        )

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = validated_data
        if password is not None:
            instance = User.objects.create(**validated_data)
            instance.set_password(password)
            instance.is_client = True
            instance.save()
        return instance
    


class UserShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'user_id',
            'full_name',
            'gender',
            'email',
            'mobile_number',
            'timestamp',
            'updated',
            'order_count',
            'password',
            'is_client',
            'is_vendor',
            'is_delivery',
            'is_newsletter',
            'is_admin'
        )

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile_number = validated_data.get('mobile_number', instance.mobile_number)
        password = validated_data.get('password', instance.password)
        instance.set_password(password)
        instance.save()
        return instance
    

class VendorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = (
            'id',
            'user',
            'added',
            'updated',
            'business_phone',
            'business_email',
            'address1',
            'address2',
            'city',
            'landmark',
            'state',
            'country',
            'pincode',
            'active'
        )




class VendorShowSerializer(serializers.ModelSerializer):
    user = UserShowSerializer(read_only=True)
    class Meta:
        model = Vendor
        fields = (
            'id',
            'user',
            'added',
            'updated',
            'business_phone',
            'business_email',
            'address1',
            'address2',
            'city',
            'landmark',
            'state',
            'country',
            'pincode',
            'active'
        )


class DeliveryBoyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryBoy
        fields = (
            'id',
            'user',
            'added',
            'updated',
            'business_phone',
            'business_email',
            'address1',
            'address2',
            'city',
            'landmark',
            'state',
            'country',
            'pincode',
            'active'
        )




class DeliveryBoyShowSerializer(serializers.ModelSerializer):
    user = UserShowSerializer(read_only=True)
    class Meta:
        model = DeliveryBoy
        fields = (
            'id',
            'user',
            'added',
            'updated',
            'business_phone',
            'business_email',
            'address1',
            'address2',
            'city',
            'landmark',
            'state',
            'country',
            'pincode',
            'active'
        )