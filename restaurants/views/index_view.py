from django.shortcuts import render, redirect
from restaurants.models.item import Item
from restaurants.models.category import Category
from restaurants.models.restaurant import Restaurant
from django.views import View
from restaurants.utils import cart_quantity
from django.contrib import messages


class Index(View):
    def get(self, request):
        cart = request.session.get('cart')

        if not cart:
            request.session['cart'] = {}
        category_id = request.GET.get('category')
        restaurant_id = request.GET.get('restaurant')
        if category_id:
            items = Item.get_items_by_category(category_id)
        elif restaurant_id:
            items = Item.get_items_by_restaurant(restaurant_id)

        else:
            items = Item.get_all_items()

        categories = Category.get_all_categories()
        restaurants = Restaurant.get_all_restaurants()
        context = {
            'items': items,
            'categories': categories,
            'restaurants': restaurants
        }
        return render(request, 'index.html', context)

    def post(self, request):
        item = request.POST.get('item')
        item_ord = Item.get_item_by_id(item)

        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        restaurant = request.POST.get('restaurant')

        if restaurant and item_ord[0].restaurant.name != restaurant:
            messages.error(request,"You have item from other restaurant in your cart.")
            return redirect('index')
        else:
            request.session['cart'] = cart_quantity(item,cart,remove)
            if remove:
                messages.error(request, "Item removed from Cart.")
            else:
                messages.success(request,"Item added to Cart.")
            return redirect('index')
