from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from cart.models import Cart
from grocery.models import Grocery, GroceryCategory

from easyeats.utils import imageUrls

def home(request):
    """
    Home page for groceries
    """
    featured = Grocery.objects.filter(featured=True, active=True)
    categories = GroceryCategory.objects.filter(active=True).order_by('name')
    grocery_list = Grocery.objects.filter(active=True).order_by('name')
    page = request.GET.get('page', 1)
    cart_obj, new_obj = Cart.objects.new_or_get(request)

    paginator = Paginator(grocery_list, 24)
    try:
        groceries = paginator.page(page)
    except PageNotAnInteger:
        groceries = paginator.page(1)
    except EmptyPage:
        groceries = paginator.page(paginator.num_pages)

    context = {
        'featured': featured,
        'groceries': groceries,
        'categories': categories,
        'cart': cart_obj,
        'image': imageUrls,
    }
    return render(request, 'grocery/home.html', context)