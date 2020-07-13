
from django.db import models
from django.db.models.signals import m2m_changed, post_save, pre_save
from django.dispatch import receiver

from products.models import Food
from accounts.models import User
from grocery.models import Grocery

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            new_obj = True
            cart_obj = self.new(user=request.user)
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class FoodEntry(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    cost = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return str(self.id)

def update_food_entry(sender, instance, **kwargs):
    line_cost = float(instance.quantity) * float(instance.food.discount_price)
    instance.cost = float(line_cost)
    instance.save
pre_save.connect(update_food_entry, sender=FoodEntry)


class GroceryEntry(models.Model):
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    cost = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return str(self.id)

def update_grocery_entry(sender, instance, **kwargs):
    line_cost = float(instance.quantity) * float(instance.grocery.discount_price)
    instance.cost = float(line_cost)
    instance.save
pre_save.connect(update_grocery_entry, sender=GroceryEntry)


class Cart(models.Model):
    """
    Cart model for handling of carts
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    foods = models.ManyToManyField(FoodEntry, blank=True)
    count = models.PositiveIntegerField(default=0)
    groceries = models.ManyToManyField(GroceryEntry, blank=True)
    sub_total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    shipping = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CartManager()



def pre_save_cart_reciever(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        foods = instance.foods.all()
        groceries = instance.groceries.all()
        sub_total = 0.00
        discount = 0.00
        for food in foods:
            sub_total += float(food.cost)
        for grocery in groceries:
            sub_total += float(grocery.cost)
        instance.sub_total = sub_total

        # calculating the shipping
        if instance.sub_total > 0:
            if instance.sub_total < 80.00:
                instance.shipping = 25.00
            elif instance.sub_total > 80.00 and instance.sub_total < 280.00:
                instance.shipping = 25.00
            else:
                instance.shipping = 25.00
        else:
            instance.shipping = 0.00

        # Checking for the user is ordering the food for first time or not
        if instance.user:
            if instance.user.order_count == 0:
                discount = instance.shipping
        instance.total = instance.shipping + instance.sub_total - discount
        instance.save()

m2m_changed.connect(pre_save_cart_reciever, sender=Cart.foods.through)
m2m_changed.connect(pre_save_cart_reciever, sender=Cart.groceries.through)

