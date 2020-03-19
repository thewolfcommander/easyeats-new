from django.shortcuts import render, redirect

from addresses.models import Address
from cart.models import Cart
from products.models import Food

from addresses.forms import AddressForm

from easyeats.utils import imageUrls


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'cart/home.html', {'cart': cart_obj, 'image': imageUrls,})


def cart_update(request):
    food_id = request.POST.get("food_id")
    food_obj = Food.objects.get(id=food_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if food_obj in cart_obj.foods.all():
        cart_obj.foods.remove(food_obj)
    else:
        cart_obj.foods.add(food_obj)
    return redirect("cart:home")



def checkout_home(request, address_id, *args, **kwargs):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    order_obj = None

    if new_obj or cart_obj.foods.count() == 0:
        return redirect("cart:home")


    address = Address.objects.get(id=address_id)
    context = {
        'cart': cart_obj,
        'address': address,
        'image': imageUrls,
    }
    return render(request, 'cart/checkout_home.html', context)

