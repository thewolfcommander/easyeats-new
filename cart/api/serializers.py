from rest_framework import serializers

from accounts.api.serializers import UserShowSerializer
from products.api.serializers import FoodSerializer
from grocery.api.serializers import GrocerySerializer

from cart.models import *
from products.models import Food
from grocery.models import Grocery


class CartListingField(serializers.RelatedField):
    def to_representation(self, value):
        return '%d' % (value.id)


class FoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodEntry
        fields = [
            'id',
            'food',
            'quantity',
            'cost'
        ]

    def create(self, validated_data):
        quantity = validated_data.get('quantity')
        food = validated_data.get('food')
        cost = float(food.discount_price * int(quantity))
        instance = FoodEntry.objects.create(food=food, quantity=quantity, cost=cost)

        return instance

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.cost = float(instance.food.discount_price)*int(instance.quantity)
        return instance


class FoodEntryShowSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)
    class Meta:
        model = FoodEntry
        fields = [
            'id',
            'food',
            'quantity',
            'cost'
        ]


class GroceryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryEntry
        fields = [
            'id',
            'grocery',
            'quantity',
            'cost'
        ]

    def create(self, validated_data):
        quantity = validated_data.get('quantity')
        grocery = validated_data.get('grocery')
        cost = float(grocery.discount_price * int(quantity))
        instance = GroceryEntry.objects.create(grocery=grocery, quantity=quantity, cost=cost)

        return instance

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.cost = float(instance.grocery.discount_price)*int(instance.quantity)
        return instance


class GroceryEntryShowSerializer(serializers.ModelSerializer):
    grocery = GrocerySerializer(read_only=True)
    class Meta:
        model = GroceryEntry
        fields = [
            'id',
            'grocery',
            'quantity',
            'cost'
        ]

    
class FoodEntryTinySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodEntry
        fields = [
            'id'
        ]


class GroceryEntryTinySerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryEntry
        fields = [
            'id'
        ]
    

class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'foods',
            'count',
            'groceries',
            'sub_total',
            'shipping',
            'total',
            'timestamp',
            'updated'
        ]

    def create(self, validated_data):
        foods = validated_data.get('foods', None)
        groceries = validated_data.get('groceries', None)
        user = validated_data.get('user', None)
        count = 0
        sub_total = 0.00
        shipping = 25.00
        total = 0.00
        discount = 0.00
        if user.order_count == 0:
            shipping = 0.00
        if foods is not None:
            for food in foods:
                sub_total = sub_total + float(food.cost)
                count += 1
        if groceries is not None:
            for grocery in groceries:
                sub_total = sub_total + float(grocery.cost)
                count += 1
        total = sub_total + shipping
        instance = Cart.objects.create(
            user=user, 
            sub_total=sub_total, 
            total=total, 
            shipping=shipping,
            count=count
        )
        if groceries is not None:
            instance.groceries.set(groceries)
        if foods is not None:
            instance.foods.set(foods)
        return instance

    def update(self, instance, validated_data):
        foods = validated_data.get('foods', None)
        groceries = validated_data.get('groceries', None)
        user = validated_data.get('user', instance.user)

        count = 0
        sub_total = 0.00
        shipping = 25.00
        total = 0.00
        discount = 0.00
        if user.order_count == 0:
            shipping = 0.00
        if foods is not None:
            for food in foods:
                sub_total = sub_total + float(food.cost)
                count += 1
        if groceries is not None:
            for grocery in groceries:
                sub_total = sub_total + float(grocery.cost)
                count += 1
        total = sub_total + shipping

        instance.user = validated_data.get('user', instance.user)
        instance.sub_total = sub_total
        instance.total = total
        instance.shipping = shipping
        instance.count = count
        instance.save()

        if groceries is not None:
            instance.groceries.set(groceries)
        if foods is not None:
            instance.foods.set(foods)
        return instance

        


    
class CartShowSerializer(serializers.ModelSerializer):
    user = UserShowSerializer(read_only=True)
    foods = FoodEntryShowSerializer(many=True, read_only=True)
    groceries = GroceryEntryShowSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'foods',
            'count',
            'groceries',
            'sub_total',
            'shipping',
            'total',
            'timestamp',
            'updated'
        ]