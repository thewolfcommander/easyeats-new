from django.shortcuts import render, redirect
from django.contrib import messages

from addresses.models import Address
from cart.models import Cart
from products.models import Food
from grocery.models import Grocery

from addresses.forms import AddressForm

from easyeats.utils import imageUrls


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    print(cart_obj.groceries.count())
    return render(request, 'cart/home.html', {'cart': cart_obj, 'image': imageUrls,})


def cart_update(request):
    food_id = request.POST.get("food_id")
    grocery_id = request.POST.get("grocery_id")
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if food_id is not None:
        food_obj = Food.objects.get(id=food_id)
        if food_obj in cart_obj.foods.all():
            cart_obj.foods.remove(food_obj)
        else:
            if food_obj.restaurant.active==False:
                messages.error(request, "The restaurant is currently Closed, Please check back later when it is open again....", extra_tags="warning")
                return redirect("core:home")
            messages.success(request, '{} is successfully added to your cart.'.format(food_obj.name), extra_tags="info")
            cart_obj.foods.add(food_obj)
    if grocery_id is not None:
        grocery_obj = Grocery.objects.get(id=grocery_id)
        if grocery_obj in cart_obj.groceries.all():
            cart_obj.groceries.remove(grocery_obj)
        else:
            messages.success(request, '{} is successfully added to your cart.'.format(grocery_obj.name), extra_tags="info")
            cart_obj.groceries.add(grocery_obj)
    
    return redirect("cart:home")



def checkout_home(request, address_id, *args, **kwargs):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    order_obj = None

    if new_obj or cart_obj.groceries.count() == 0 and cart_obj.foods.count() == 0:
        return redirect("cart:home")

    address = Address.objects.get(id=address_id)
    context = {
        'cart': cart_obj,
        'address': address,
        'image': imageUrls,
    }
    return render(request, 'cart/checkout_home.html', context)

