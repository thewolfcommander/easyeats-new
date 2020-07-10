from rest_framework import serializers

from products.models import *


class RestaurantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = [
            'image',
            'is_featured'
        ]



class RestaurantSerializer(serializers.ModelSerializer):
    images = RestaurantImageSerializer(read_only=True, many=True)
    class Meta:
        model = Restaurant
        fields = [
            'id',
            'added',
            'updated',
            'name',
            'address1',
            'address2',
            'city',
            'landmark',
            'state',
            'country',
            'pincode',
            'mobile_number',
            'email',
            'active',
            'vendor',
            'images'
        ]

    
class CategorySerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    class Meta:
        model = Category
        fields = [
            'id',
            'image',
            'name',
            'restaurant',
            'summary',
            'description',
            'active',
            'added',
            'updated'
        ]


class FoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodImage
        fields = [
            'image',
            'is_featured'
        ]

    
class FoodTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTag
        fields = [
            'name'
        ]

    
class FoodSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    images = FoodImageSerializer(read_only=True, many=True)
    tags = FoodTagSerializer(read_only=True, many=True)
    class Meta:
        model = Food
        fields = [
            'id',
            'category',
            'name',
            'summary',
            'description',
            'active',
            'added',
            'updated',
            'gross_price',
            'discount_price',
            'original_price',
            'tax',
            'preparation_time',
            'added_by',
            'featured',
            'restaurant',
            'images',
            'tags'
        ]



class FoodReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodReview
        fields = [
            'id',
            'food',
            'comment',
            'rating_1',
            'added',
            'user'
        ]

    

class RestaurantReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantReview
        fields = [
            'id',
            'restaurant',
            'comment',
            'rating_1',
            'added',
            'user'
        ]