from django.db import models
from django.db.models.signals import m2m_changed

from products.models import Food
from accounts.models import User

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

class Cart(models.Model):
    """
    Cart model for handling of carts
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    foods = models.ManyToManyField(Food)
    sub_total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    shipping = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CartManager()


def pre_save_cart_reciever(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        foods = instance.foods.all()
        sub_total = 0.00
        for food in foods:
            sub_total += float(food.discount_price)
        instance.sub_total = sub_total

        # calculating the shipping
        if instance.sub_total > 0:
            if instance.sub_total < 80.00:
                instance.shipping = 25.00
            elif instance.sub_total > 80.00 and instance.sub_total < 280.00:
                instance.shipping = 30.00
            else:
                instance.shipping = 25.00
        else:
            instance.shipping = 0.00

        # Checking for the user is ordering the food for first time or not
        if instance.user:
            if instance.user.order_count == 0:
                instance.shipping = 0.00
        instance.total = instance.shipping + instance.sub_total
        instance.save()

m2m_changed.connect(pre_save_cart_reciever, sender=Cart.foods.through)