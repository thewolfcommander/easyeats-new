from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login

from social_django.models import UserSocialAuth

from .forms import *
from addresses.models import Address
from addresses.forms import AddressForm
from orders.models import Order


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('core:home')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def myaccount(request):
    user = request.user
    if user.is_delivery:
        new_orders = Order.objects.filter(status="created")
        if new_orders.exists():
            messages.info(request, "You have {} new orders. Handle it now. {}".format(new_orders.count(), new_orders.first().updated), extra_tags="info")
    if request.method == 'POST':
        form = UserDetailForm(request.POST or None, instance=user)
        if form.is_valid():
            usr = form.save(commit=False)
            usr.save()
            return redirect(request.path_info)
        messages.success(request, "You have successfully updated", extra_tags="success")
    else:
        form = UserDetailForm(instance=user)
    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'accounts/myaccount/home.html', context)


@login_required
def addresses(request):
    if request.user.is_delivery:
        new_orders = Order.objects.filter(status="created")
        if new_orders.exists():
            messages.info(request, "You have {} new orders. Handle it now. {}".format(new_orders.count(), new_orders.first().updated), extra_tags="info")
    addresses = Address.objects.filter(user=request.user)
    context = {
        'addresses': addresses
    }
    return render(request, 'accounts/myaccount/addresses.html', context)


@login_required
def address_detail(request, pk=None, *args, **kwargs):
    if request.user.is_delivery:
        new_orders = Order.objects.filter(status="created")
        if new_orders.exists():
            messages.info(request, "You have {} new orders. Handle it now. {}".format(new_orders.count(), new_orders.first().updated), extra_tags="info")
    address = get_object_or_404(Address, id=pk)
    if address.user == request.user:
        if request.method == 'POST':
            form = AddressForm(request.POST or None, instance=address)
            if form.is_valid():
                add = form.save(commit=False)
                add.save()
                return redirect(request.path_info)
        else:
            form = AddressForm(instance=address)

        context = {
            'form': form,
            'address': address
        }
    else:
        return redirect('accounts:addresses')
        context = {}
    return render(request, 'accounts/myaccount/address_detail.html', context)

@login_required
def delete_address(request, pk=None, *args, **kwargs):
    address = get_object_or_404(Address, id=pk)
    if address.user == request.user:
        address.delete()
    return redirect("accounts:addresses")


@login_required
def orders(request):
    if request.user.is_delivery:
        new_orders = Order.objects.filter(status="created")
        if new_orders.exists():
            messages.info(request, "You have {} new orders. Handle it now. {}".format(new_orders.count(), new_orders.first().updated), extra_tags="info")
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': orders,
    }
    return render(request, 'accounts/myaccount/orders.html', context)



@login_required
def order_detail(request, pk=None, *args, **kwargs):
    if request.user.is_delivery:
        new_orders = Order.objects.filter(status="created")
        if new_orders.exists():
            messages.info(request, "You have {} new orders. Handle it now. {}".format(new_orders.count(), new_orders.first().updated), extra_tags="info")
    order = get_object_or_404(Order, id=pk)
    context = {
        'order': order,
    }
    return render(request, 'accounts/myaccount/order_detail.html', context)


@login_required
def settings(request):
    user = request.user
    if request.user.is_delivery:
        new_orders = Order.objects.filter(status="created")
        if new_orders.exists():
            messages.info(request, "You have {} new orders. Handle it now. {}".format(new_orders.count(), new_orders.first().updated), extra_tags="info")
    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'accounts/myaccount/settings.html', {
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })


@login_required
def password(request):
    if request.user.is_delivery:
        new_orders = Order.objects.filter(status="created")
        if new_orders.exists():
            messages.info(request, "You have {} new orders. Handle it now. {}".format(new_orders.count(), new_orders.first().updated), extra_tags="info")
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm
    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'accounts/myaccount/password.html', {'form': form})