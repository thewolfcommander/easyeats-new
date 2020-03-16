from django.shortcuts import render, redirect, get_object_or_404

from django_slack import slack_message

from orders.models import Order, CashBack
from addresses.models import Address
from cart.models import Cart
# Create your views here.

def create_order(request):
    cart_id = request.POST.get('cart_id')
    address_id = request.POST.get('address_id')
    cart = Cart.objects.get(id=cart_id)
    address = Address.objects.get(id=address_id)
    user = request.user
    prev_order = Order.objects.filter(cart=cart_id, user=user, address_id=address_id)
    if prev_order.exists():
        return redirect("orders:failed")
    order = Order.objects.create(user=user, cart=cart, address=address)
    order.update_total()
    order.user.order_count += 1
    order.user.save()
    slack_message('notifications/ordered.slack', {
        'order': order,
        'user': request.user,
    })
    print("Session ID before: {}".format(request.session["cart_id"]))
    del request.session["cart_id"]
    return redirect("orders:success")


def order_success(request):
    return render(request, 'orders/success.html')

def order_failed(request):
    return render(request, 'orders/failed.html')