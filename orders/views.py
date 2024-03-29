import json
import requests

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    print("Session ID before: {}".format(request.session["cart_id"]))
    del request.session["cart_id"]
    text = "{} ==> Order with ID - {}, USER - {}, STATUS - {}, SHIPPING TOTAL - {}, TOTAL - {}, placed at {} awaiting for response. Please check the admin panel.".format(order.id, order.order_id, order.user.user_id, order.status, order.shipping_total, order.total, order.timestamp)
    try:
        data = {
            "text": text
        }
        resp = requests.post('https://hooks.slack.com/services/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', json.dumps(data))
        print(resp.json())
    except:
        print("Error")
    return redirect("orders:success")

@login_required
def order_success(request):
    messages.success(request, 'Your order created successfully...', extra_tags="success")
    return render(request, 'orders/success.html')

@login_required
def order_failed(request):
    messages.error(request, 'Your order failed, we seriously get into it very soon...', extra_tags="danger")
    return render(request, 'orders/failed.html')