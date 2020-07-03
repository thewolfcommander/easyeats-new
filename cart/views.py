from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

from addresses.models import Address
from cart.models import Cart, FoodEntry, GroceryEntry
from products.models import Food
from grocery.models import Grocery

from addresses.forms import AddressForm

from easyeats.utils import imageUrls


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'cart/home.html', {'cart': cart_obj, 'image': imageUrls,})


def add_to_cart(request):
    food_id = request.POST.get("food_id")
    grocery_id = request.POST.get("grocery_id")
    food_quantity = request.POST.get("food_quantity")
    grocery_quantity = request.POST.get("grocery_quantity")
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    
    if food_id is not None and food_quantity is not None:
        food_entry = Food.objects.get(id=food_id)
        food_obj = FoodEntry.objects.get_or_create(food=food_entry, quantity=food_quantity)[0]
        if food_obj in cart_obj.foods.all():
            food_obj.quantity += int(food_quantity)
            food_obj.save()
            cart_obj.foods.add(food_obj)
        else:
            if food_obj.food.restaurant.active==False:
                messages.error(request, "The restaurant is currently Closed, Please check back later when it is open again....", extra_tags="warning")
                return redirect("core:home")
            messages.success(request, '{} is successfully added to your cart.'.format(food_obj.food.name), extra_tags="info")
            cart_obj.foods.add(food_obj)

    if grocery_id is not None and grocery_quantity is not None:
        grocery_entry = Grocery.objects.get(id=grocery_id)
        grocery_obj = GroceryEntry.objects.get_or_create(grocery=grocery_entry, quantity=grocery_quantity)[0]
        if grocery_obj in cart_obj.groceries.all():
            grocery_obj.quantity += int(grocery_quantity)
            grocery_obj.save()
            cart_obj.groceries.add(grocery_obj)
            messages.success(request, '{} is successfully added to your cart.'.format(grocery_obj.grocery.name), extra_tags="info")
        else:
            cart_obj.groceries.add(grocery_obj)
            messages.success(request, '{} is successfully added to your cart.'.format(grocery_obj.grocery.name), extra_tags="info")
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def remove_from_cart(request):
    food_id = request.POST.get("food_id")
    grocery_id = request.POST.get("grocery_id")
    # food_quantity = 2
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if food_id is not None:
        food_entry = Food.objects.get(id=food_id)
        food_objs = FoodEntry.objects.filter(food=food_entry)
        for food_obj in food_objs:
            cart_obj.foods.remove(food_obj)
            messages.success(request, '{} is successfully removed from your cart.'.format(food_obj.food.name), extra_tags="info")
    if grocery_id is not None:
        grocery_entry = Grocery.objects.get(id=grocery_id)
        grocery_objs = GroceryEntry.objects.filter(grocery=grocery_entry)
        for grocery_obj in grocery_objs:
            cart_obj.groceries.remove(grocery_obj)
            messages.success(request, '{} is successfully removed from your cart.'.format(grocery_obj.grocery.name), extra_tags="info")
    return redirect("cart:home")


def cart_update(request):
    food_id = request.POST.get("food_id")
    grocery_id = request.POST.get("grocery_id")
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if food_id is not None:
        food_entry = Food.objects.get(id=food_id)
        food_obj = FoodEntry.objects.get_or_create(food=food_entry, quantity=3)[0]
        if food_obj in cart_obj.foods.all():
            cart_obj.foods.remove(food_obj)
        else:
            if food_obj.food.restaurant.active==False:
                messages.error(request, "The restaurant is currently Closed, Please check back later when it is open again....", extra_tags="warning")
                return redirect("core:home")
            messages.success(request, '{} is successfully added to your cart.'.format(food_obj.food.name), extra_tags="info")
            cart_obj.foods.add(food_obj)
    if grocery_id is not None:
        grocery_entry = Grocery.objects.get(id=grocery_id)
        grocery_obj = GroceryEntry.objects.create(grocery=grocery_entry, quantity=3)
        if grocery_obj in cart_obj.groceries.all():
            cart_obj.groceries.remove(grocery_obj)
        else:
            messages.success(request, '{} is successfully added to your cart.'.format(grocery_obj.grocery.name), extra_tags="info")
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

