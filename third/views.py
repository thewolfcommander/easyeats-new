from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts.models import User, Vendor, DeliveryBoy
from accounts.forms import VendorForm, DeliveryBoyForm

from products.models import Restaurant

from orders.models import Order

@login_required
def vendor_home(request):
    user = Vendor.objects.filter(user=request.user)
    if user.exists():
        vendor = user.first()
        if request.method == 'POST':
            form = VendorForm(request.POST or None, instance=vendor)
            if form.is_valid():
                form.save()
        else:
            form = VendorForm(instance=vendor)
    else:
        vendor = request.user
    
    context = {
        'vendor': vendor,
        'form': form,
    }
    return render(request, 'third/vendor/home.html', context)



@login_required
def vendor_restaurants(request):
    vendor = Vendor.objects.filter(user=request.user).first()
    restaurants = Restaurant.objects.filter(vendor=vendor)
    context = {
        'restaurants': restaurants
    }
    return render(request, 'third/vendor/restaurants.html', context)


@login_required
def vendor_restaurant_detail(request, pk=None, *args, **kwargs):
    restaurant = get_object_or_404(Restaurant, id=pk)
    context = {
        'restaurant': restaurant,
    }
    return render(request, 'third/vendor/restaurant_detail.html', context)



@login_required
def delivery_home(request):
    user = DeliveryBoy.objects.filter(user=request.user)
    if user.exists():
        delivery = user.first()
        if request.method == 'POST':
            form = DeliveryBoyForm(request.POST or None, instance=delivery)
            if form.is_valid():
                form.save()
        else:
            form = DeliveryBoyForm(instance=delivery)
    else:
        delivery = request.user
    
    context = {
        'delivery': delivery,
        'form': form,
    }
    return render(request, 'third/delivery/home.html', context)


@login_required
def new_delivery(request):
    title = 'New Deliveries'
    orders = Order.objects.filter(status='created').order_by('-updated')
    context = {
        'orders': orders,
        'title': title,
    }
    return render(request, 'third/delivery/delivery.html', context)


@login_required
def shipped_delivery(request):
    title = 'Shipped Deliveries'
    orders = Order.objects.filter(status='shipped').order_by('-updated')
    context = {
        'orders': orders,
        'title': title,
    }
    return render(request, 'third/delivery/delivery.html', context)


@login_required
def completed_delivery(request):
    title = 'Completed Deliveries'
    orders = Order.objects.filter(status='delivered').order_by('-updated')
    context = {
        'orders': orders,
        'title': title,
    }
    return render(request, 'third/delivery/delivery.html', context)


@login_required
def cancelled_delivery(request):
    title = 'Cancelled Deliveries'
    orders = Order.objects.filter(status='cancelled').order_by('-updated')
    context = {
        'orders': orders,
        'title': title,
    }
    return render(request, 'third/delivery/delivery.html', context)


@login_required
def ship_delivery(request, pk=None, *args, **kwargs):
    order = get_object_or_404(Order, id=pk)
    order.status = 'shipped'
    return redirect('third:shipped_delivery')



@login_required
def complete_delivery(request, pk=None, *args, **kwargs):
    order = get_object_or_404(Order, id=pk)
    order.status = 'completed'
    return redirect('third:completed_delivery')




@login_required
def cancel_delivery(request, pk=None, *args, **kwargs):
    order = get_object_or_404(Order, id=pk)
    order.status = 'completed'
    return redirect('third:completed_delivery')