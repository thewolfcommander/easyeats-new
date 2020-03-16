import math

from django.db import models
from django.db.models.signals import pre_save, post_save

from accounts.models import User, DeliveryBoy
from addresses.models import Address
from cart.models import Cart

from easyeats.utils import unique_order_id_generator

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
    ('refunded', 'Refunded'),
)

class OrderManager(models.Manager):
    def new_or_get(self, user, cart_obj, address):
        created = False
        qs = self.get_queryset().filter(
                user=user, 
                cart=cart_obj, 
                active=True,
                status='created'
            )
        if qs.count() == 1:
            obj = qs.first()
        else:
            obj = self.model.objects.create(
                    user=user, 
                    cart=cart_obj,
                    address=address)
            created = True
        return obj, created


class Order(models.Model):
    """
    This model gonna handle orders across the platform
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_boy = models.ForeignKey(DeliveryBoy, on_delete=models.CASCADE, null=True, blank=True)
    order_id = models.CharField(max_length=120, blank=True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total      = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total               = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    restaurant_part = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    active              = models.BooleanField(default=True)
    updated             = models.DateTimeField(auto_now=True)
    timestamp           = models.DateTimeField(auto_now_add=True)

    objects = OrderManager()

    def __str__(self):
        return self.order_id

    class Meta:
       ordering = ['-timestamp', '-updated']

    def get_absolute_url(self):
        return reverse("orders:detail", kwargs={'order_id': self.order_id})

    def get_status(self):
        if self.status == "created":
            return "Created successfully"
        elif self.status == "shipped":
            return "Shipped"
        elif self.status == "delivered":
            return "Delivered"
        elif self.status == "cancelled":
            return "Cancelled"
        elif self.status == "refunded":
            return "Refunded"
        return "Shipping Soon"

    def update_total(self):
        cart_total = self.cart.total
        shipping_total = 0.00
        new_total = math.fsum([cart_total, shipping_total])
        formatted_total = format(new_total, '.2f')
        self.total = formatted_total
        self.shipping_total = shipping_total
        self.save()
        return new_total

    def calc_rest_part(self):
        order_total = self.total
        commission = (10*float(order_total))/100
        self.restaurant_part = float(order_total) - float(commission)
        

def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
    qs = Order.objects.filter(cart=instance.cart).exclude(user=instance.user)
    if qs.exists():
        qs.update(active=False)


pre_save.connect(pre_save_create_order_id, sender=Order)


def post_save_order(sender, instance, created, *args, **kwargs):
    #print("running")
    if created:
        print("Updating... first")
        instance.update_total()
        instance.calc_rest_part()


post_save.connect(post_save_order, sender=Order)