from django.db import models
from accounts.models import User

class GroceryCategory(models.Model):
    """
    Model for defining the categories of the groceries
    """
    image = models.ImageField(upload_to='grocery_category_feature_image', null=True)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    active = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Grocery Category'
        verbose_name_plural = 'Grocery Categories'

    def __str__(self):
        return '{} - {}'.format(str(self.id), self.name)

    
class Grocery(models.Model):
    """
    Model for defining the Grocery Information
    """
    grocery_category = models.ManyToManyField(GroceryCategory)
    name = models.CharField(max_length=255, null=True)
    summary = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    active = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    gross_price = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    discount_price = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    original_price = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    tax = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ('updated',)
        verbose_name = "Grocery Item"
        verbose_name_plural = "Grocery Items"


    def get_absolute_url(self):
        # return reverse("products:food_detail", kwargs={"id": self.id})
        pass

    def __str__(self):
        return self.name


class GroceryImage(models.Model):
    """
    This model gonna hold the gallery images for a particular grocery product
    """
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='grocery_images', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.grocery.name
        

    
class GroceryTag(models.Model):
    """
    This model is for the common tags between the grocery items
    """
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class GroceryReview(models.Model):
    """
    This model is for the reviews for the particular grocery products
    """
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, null=True)
    rating_1 = models.BooleanField(default=False)
    rating_2 = models.BooleanField(default=False)
    rating_3 = models.BooleanField(default=False)
    rating_4 = models.BooleanField(default=False)
    rating_5 = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.grocery.name