from rest_framework import serializers

from grocery.models import *



class GroceryCategoryShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryCategory
        fields = [
            'id',
            'image',
            'name',
            'active',
            'added',
            'updated',
        ]


class GrocerySubCategoryTinySerializer(serializers.ModelSerializer):
    category = GroceryCategoryShowSerializer(read_only=True)
    class Meta:
        model = GrocerySubCategory
        fields = [
            'id',
            'category',
            'image',
            'name',
            'active',
            'added',
            'updated'
        ]


class GrocerySubCategoryShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrocerySubCategory
        fields = [
            'id',
            'image',
            'name',
            'active',
            'added',
            'updated'
        ]


class GroceryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryCategory
        fields = [
            'id',
            'image',
            'name',
            'active',
            'added',
            'updated',
        ]

    
class GroceryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryImage
        fields = [
            'image',
            'is_featured'
        ]

    
class GroceryTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryTag
        fields = [
            'name',
        ]

    
class GrocerySerializer(serializers.ModelSerializer):
    grocery_category = GroceryCategoryShowSerializer(read_only=True)
    sub_category = GrocerySubCategoryShowSerializer(read_only=True)
    images = GroceryImageSerializer(many=True, read_only=True)
    tags = GroceryTagSerializer(many=True, read_only=True)
    class Meta:
        model = Grocery
        fields = [
            'id',
            'grocery_category',
            'sub_category',
            'name',
            'quantity',
            'scale',
            'active',
            'added',
            'updated',
            'gross_price',
            'discount_price',
            'original_price',
            'tax',
            'added_by',
            'featured',
            'images',
            'tags'
        ]


class GroceryReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryReview
        fields = [
            'id',
            'grocery',
            'comment',
            'rating_1',
            'added',
            'user'
        ]


class GroceryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryRequest
        fields = [
            'id',
            'name',
            'phone_number',
            'info',
            'added',
            'updated',
            'fullfilled'
        ]