from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from addresses.forms import AddressForm
from addresses.models import Address
# Create your views here.

@login_required
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST or None)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('addresses:select')
    else:
        form = AddressForm()
    context = {
        'form': form,
    }
    return render(request, 'addresses/add.html', context)

@login_required
def select_address(request):
    addresses = Address.objects.filter(user=request.user)
    context = {
        'addresses': addresses,
    }
    return render(request, 'addresses/select.html', context)