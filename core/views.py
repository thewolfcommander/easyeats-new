from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.contrib.auth.decorators import login_required

from accounts.forms import VendorForm, DeliveryBoyForm
from accounts.models import Vendor, DeliveryBoy
from core.forms import (
    ContactForm,
    ReportIssueForm,
    NewsletterForm,
)
from cart.models import Cart
from easyeats import utils
from products.models import (
    Restaurant,
    Category,
    Food,
    Collection,
    RestaurantImage,
    FoodImage
)

def search(request):
    if request.method == 'GET':
        query = request.GET.get("search")
        restaurants = Restaurant.objects.filter(
            Q(name__icontains=query) |
            Q(city__icontains=query)
        )
        featured_foods = Food.objects.filter(active=True, featured=True).order_by('-updated')[:3]
        foods_list = Food.objects.filter(
            Q(name__icontains=query) |
            Q(summary__icontains=query) |
            Q(category__name__icontains=query) |
            Q(foodtag__name__icontains=query)
        )
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        page = request.GET.get('page', 1)

        paginator = Paginator(foods_list, 12)
        try:
            foods = paginator.page(page)
        except PageNotAnInteger:
            foods = paginator.page(1)
        except EmptyPage:
            foods = paginator.page(paginator.num_pages)
        f_count =foods_list.count()
        r_count = restaurants.count()
        context = {
            'query': query,
            'restaurants': restaurants,
            'featured_foods': featured_foods,
            'foods': foods,
            'count': int(f_count) + int(r_count), 
            'cart': cart_obj,
        }
    return render(request, 'core/search.html', context)


def home(request):
    restaurants = Restaurant.objects.filter(active=True).order_by('-updated')[:10]
    categories = Category.objects.filter(active=True).order_by('-updated')[:10]
    featured_foods = Food.objects.filter(active=True, featured=True).order_by('-updated')[:3]
    foods = Food.objects.filter(active=True).order_by('-updated')[:16]
    collections = Collection.objects.filter(active=True).order_by('-updated')[:10]
    context = {
        'restaurants': restaurants,
        'categories': categories,
        'featured_foods': featured_foods,
        'foods': foods,
        'collections': collections,
    }
    return render(request, 'core/home.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact = form.save(commit=False)
            client_address = utils.get_client_ip(request)
            print(client_address)
            contact.ip_address = client_address
            contact.save()
            return redirect("core:home")
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'core/contact.html', context)


def report(request):
    if request.method == 'POST':
        form = ReportIssueForm(request.POST or None)
        if form.is_valid():
            report = form.save(commit=False)
            client_address = utils.get_client_ip(request)
            print(client_address)
            report.ip_address = client_address
            report.save()
            return redirect("core:home")
    else:
        form = ReportIssueForm()
    context = {
        'form': form,
    }
    return render(request, 'core/report.html', context)


def about(request):
    featured_foods = Food.objects.filter(active=True, featured=True).order_by('-updated')[:3]
    context = {
        'featured_foods': featured_foods,
    }
    return render(request, 'core/about.html', context)


def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')


def partner_relations(request):
    return render(request, 'core/partner_relations.html')


def terms_of_service(request):
    return render(request, 'core/terms_of_service.html')

@login_required
def join_as_vendor(request):
    vendor = Vendor.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = VendorForm(request.POST or None)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.user = request.user
            vendor.active = False
            vendor.save()
            return redirect('accounts:settings')
    else:
        form = VendorForm()
    context = {
        'form': form,
        'vendor': vendor,
    }
    return render(request, 'core/join_as_vendor.html', context)


@login_required
def join_as_delivery_boy(request):
    delivery_boy = DeliveryBoy.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = DeliveryBoyForm(request.POST or None)
        if form.is_valid():
            delivery_boy = form.save(commit=False)
            delivery_boy.user = request.user
            delivery_boy.active = False
            delivery_boy.save()
            return redirect('accounts:settings')
    else:
        form = DeliveryBoyForm()
    context = {
        'form': form,
        'delivery_boy': delivery_boy,
    }
    return render(request, 'core/join_as_delivery_boy.html', context)


def best_offer(request):
    return render(request, 'core/best_offer.html')