from django.shortcuts import render, redirect
from restaurants.models.item import Item
from restaurants.models.category import Category
from restaurants.models.restaurant import Restaurant
from django.views import View


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

        cart = request.session.get('cart')
        remove = request.POST.get('remove')

        if cart:
            quantity = cart.get(item)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(item)
                    else:
                        cart[item] = quantity-1
                else:
                    cart[item] = quantity+1
            else:
                cart[item] = 1
        else:
            cart = {}
            cart[item] = 1

        request.session['cart'] = cart

        return redirect('index')
