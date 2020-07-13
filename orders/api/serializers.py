from rest_framework import serializers

from orders.models import *
from cart.api.serializers import CartShowSerializer
from accounts.api.serializers import UserShowSerializer, DeliveryBoyShowSerializer
from addresses.api.serializers import AddressSerializer


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'order_id',
            'user',
            'delivery_boy',
            'address',
            'cart',
            'status',
            'shipping_total',
            'total',
            'restaurant_part',
            'active',
            'updated',
            'timestamp'
        ]

    def create(self, validated_data):
        cart = validated_data.get('cart', None)

        shipping_total = 0.00
        discount = 0.00
        total = 0.00

        if cart is not None:
            shipping_total = cart.shipping
            total = cart.total
        
        instance = Order.objects.create(
                **validated_data, 
                shipping_total = shipping_total,
                discount = discount,
                total = total,
                status = "created"
            )

        return instance

    
    def update(self, instance, validated_data):
        instance.delivery_boy = validated_data.get('delivery_boy', instance.delivery_boy)
        instance.address = validated_data.get('address', instance.address)
        instance.status = validated_data.get('status', instance.status)
        instance.active = validated_data.get('active', instance.active)
        instance.save()

        return instance


    
class OrderShowSerializer(serializers.ModelSerializer):
    user = UserShowSerializer(read_only=True)
    delivery_boy = DeliveryBoyShowSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    cart = CartShowSerializer(read_only=True)
    class Meta:
        model = Order
        fields = [
            'id',
            'order_id',
            'user',
            'delivery_boy',
            'address',
            'cart',
            'status',
            'shipping_total',
            'total',
            'restaurant_part',
            'active',
            'updated',
            'timestamp'
        ]