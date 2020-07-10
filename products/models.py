from django.db import models

from accounts.models import (
    User,
    Vendor
)

class Restaurant(models.Model):
    """
    This model keeps the data about restaurants
    """
    STATE_CHOICES = [
        ('uttarakhand', 'Uttarakhand'),
    ]
    COUNTRY_CHOICES = [
        ('india', 'India'),
    ]
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, null=True)
    address1 = models.CharField(max_length=255, null=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True)
    landmark = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, choices=STATE_CHOICES, default='uttarakhand')
    country = models.CharField(max_length=255, null=True, choices=COUNTRY_CHOICES, default='india')
    pincode = models.CharField(max_length=6, null=True)
    mobile_number = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=255, null=True)
    active = models.BooleanField(default=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    class Meta:
        ordering = ('vendor',)
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return self.name

    @property
    def images(self):
        return self.restaurantimage_set.all()


class RestaurantImage(models.Model):
    """
    This model gonna hold the gallery images for a particular restaurant
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='restaurant_images', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.restaurant.name


class Category(models.Model):
    """
    This model gonna hold the available categories for a particular restaurant
    """
    image = models.ImageField(upload_to='category_feature_image', null=True)
    name = models.CharField(max_length=255, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=4)
    summary = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    active = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Food Category'
        verbose_name_plural = 'Food Categories'

    def __str__(self):
        return '{} - {}'.format(str(self.id), self.name)


class Collection(models.Model):
    """
    This model gonna hold the featured collections on the platform
    """
    image = models.ImageField(upload_to='collection_feature_image', null=True)
    name = models.CharField(max_length=255, null=True)
    summary = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    active = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Food Collection'
        verbose_name_plural = 'Food Collections'

    def __str__(self):
        return self.name

    
class Food(models.Model):
    """
    This model gonna hold the available food items for a particular category and a particular restaurant
    """
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=255, null=True)
    summary = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    active = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    gross_price = models.CharField(max_length=255, null=True)
    discount_price = models.CharField(max_length=255, null=True)
    original_price = models.CharField(max_length=255, null=True)
    tax = models.CharField(max_length=255, null=True)
    preparation_time = models.CharField(max_length=5, null=True, help_text="In minutes")
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    featured = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ('updated',)
        verbose_name = "Food Item"
        verbose_name_plural = "Food Items"


    def get_absolute_url(self):
        return reverse("products:food_detail", kwargs={"id": self.id})

    
    @property
    def images(self):
        return self.foodimage_set.all()

    
    @property
    def tags(self):
        return self.foodtag_set.all()


class FoodImage(models.Model):
    """
    This model gonna hold the gallery images for a particular food product
    """
    food = models.ForeignKey(Food, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='food_images', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.food.name
        

    
class FoodTag(models.Model):
    """
    This model is for the common tags between the foods
    """
    food = models.ForeignKey(Food, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class Review(models.Model):
    """
    This model is for the reviews for the particular products
    """
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, null=True)
    rating_1 = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.food.name



class RestaurantReview(models.Model):
    """
    This model is for the reviews for the particular products
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, null=True)
    rating_1 = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant.name

    