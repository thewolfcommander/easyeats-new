from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from cart.models import Cart
from products.models import *
from products.forms import *


def menu(request):
    featured_foods = Food.objects.filter(active=True, featured=True).order_by('-updated')[:3]
    food_list = Food.objects.filter(active=True)
    page = request.GET.get('page', 1)
    cart_obj, new_obj = Cart.objects.new_or_get(request)

    paginator = Paginator(food_list, 12)
    try:
        foods = paginator.page(page)
    except PageNotAnInteger:
        foods = paginator.page(1)
    except EmptyPage:
        foods = paginator.page(paginator.num_pages)

    context = {
        'featured_foods': featured_foods,
        'foods': foods,
        'cart': cart_obj
    }
    return render(request, 'products/menu.html', context)


def food_detail(request, pk=None, *args, **kwargs):
    featured_foods = Food.objects.filter(active=True, featured=True).order_by('-updated')[:3]
    food = get_object_or_404(Food, id=pk)
    if food:
        if request.method == 'POST':
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.food = food
                review.save()
                return redirect(request.path_info)
            messages.success(request, "You have successfully submitted a review", extra_tags="success")
        else:
            form = ReviewForm()
            messages.success(request, "Review not submitted", extra_tags="danger")
        reviews = Review.objects.filter(food=food)
        categories = Category.objects.filter(food=food)
        tags = FoodTag.objects.filter(food=food)
        recommendations = Food.objects.filter(restaurant=food.restaurant)[:4]
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context = {
            'food': food,
            'tags': tags,
            'categories': categories,
            'featured_foods': featured_foods,
            'recommendations': recommendations,
            'form': form,
            'reviews': reviews,
            'cart': cart_obj,
        }
    else:
        context = {
            'featured_foods': featured_foods,
        }
    return render(request, 'products/food_detail.html', context)


def restaurant_list(request):
    restaurants = Restaurant.objects.filter(active=True)
    featured_foods = Food.objects.filter(active=True, featured=True).order_by('-updated')[:3]
    context = {
        'restaurants': restaurants,
        'featured_foods': featured_foods,
    }
    return render(request, 'products/restaurant_list.html', context)


def restaurant_detail(request, pk=None, *args, **kwargs):
    restaurant = get_object_or_404(Restaurant, id=pk)
    foods = Food.objects.filter(active=True, restaurant=restaurant).order_by('-updated')
    featured_foods = Food.objects.filter(active=True, featured=True).order_by('-updated')[:3]
    if request.method == 'POST':
        form = RestaurantReviewForm(request.POST or None)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.restaurant = restaurant
            review.save()
            return redirect(request.path_info)
        messages.success(request, "You have successfully submitted a review", extra_tags="success")
    else:
        form = RestaurantReviewForm()
        messages.success(request, "Review not submitted", extra_tags="danger")
    reviews = RestaurantReview.objects.filter(restaurant=restaurant)
    context = {
        'restaurant': restaurant,
        'featured_foods': featured_foods,
        'foods': foods,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'products/restaurant_detail.html', context)


def categories_list(request):
    categories = Category.objects.filter(active=True)
    featured_foods = Food.objects.filter(active=True, featured=True).order_by('-updated')[:3]
    context = {
        'categories': categories,
        'featured_foods': featured_foods
    }
    return render(request, 'products/category_list.html', context)


def categories_detail(request, pk=None, *args, **kwargs):
    category = get_object_or_404(Category, id=pk)
    featured_foods = Food.objects.filter(active=True, featured=True).order_by('-updated')[:3]
    foods = Food.objects.filter(category__name__iexact=category.name)
    context = {
        'category': category,
        'featured_foods': featured_foods,
        'foods': foods,
    }
    return render(request, 'products/category_detail.html', context)


def collection_list(request):
    collections = Collection.objects.filter(active=True)
    featured_foods = Food.objects.filter(active=True, featured=True).order_by('-updated')[:3]
    context = {
        'collections': collections,
        'featured_foods': featured_foods
    }
    return render(request, 'products/collection_list.html', context)


def collection_detail(request, pk=None, *args, **kwargs):
    collection = get_object_or_404(Collection, id=pk)
    featured_foods = Food.objects.filter(active=True, featured=True).order_by('-updated')[:3]
    foods = Food.objects.filter(collection=collection)
    context = {
        'collection': collection,
        'featured_foods': featured_foods,
        'foods': foods,
    }
    return render(request, 'products/collection_detail.html', context)