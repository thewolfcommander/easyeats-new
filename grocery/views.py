from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from cart.models import Cart
from grocery.models import Grocery, GroceryCategory, GrocerySubCategory

from easyeats.utils import imageUrls

def home(request):
    """
    Home page for groceries
    """
    categories = GroceryCategory.objects.filter(active=True)
    sub_categories = GrocerySubCategory.objects.filter(active=True)
    grocery_list = Grocery.objects.filter(active=True)
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
        'groceries': groceries,
        'categories': categories,
        'cart': cart_obj,
        'image': imageUrls,
        'sub_categories': sub_categories,
    }
    return render(request, 'grocery/home.html', context)


def category_detail(request, pk=None, *args, **kwargs):
    """
    Detail page for Grocery Categories
    """
    category = get_object_or_404(GroceryCategory, id=pk)
    sub_categories = GrocerySubCategory.objects.filter(category=category)
    categories = GroceryCategory.objects.filter(active=True)
    groceries = Grocery.objects.filter(active=True)
    cart_obj, new_obj = Cart.objects.new_or_get(request)

    context = {
        'groceries': groceries,
        'category': category,
        'cart': cart_obj,
        'image': imageUrls,
        'sub_categories': sub_categories,
        'categories': categories,
    }
    return render(request, 'grocery/category_detail.html', context)


def subcategory_detail(request, pk=None, *args, **kwargs):
    """
    Detail Page for Grocery Sub categories
    """
    sub_category = get_object_or_404(GrocerySubCategory, id=pk)
    groceries = Grocery.objects.filter(active=True, sub_category=sub_category)
    cart_obj, new_obj = Cart.objects.new_or_get(request)

    context = {
        'groceries': groceries,
        'sub_category': sub_category,
        'cart': cart_obj,
        'image': imageUrls,
    }
    return render(request, 'grocery/subcategory_detail.html', context)


def grocery_detail(request, pk=None, *args, **kwargs):
    """
    Detail Page for Groceries
    """
    grocery = get_object_or_404(Grocery, id=pk)
    cart_obj, new_obj = Cart.objects.new_or_get(request)

    context = {
        'groceries': groceries,
        'cart': cart_obj,
        'image': imageUrls,
    }
    return render(request, 'grocery/grocery_detail.html', context)