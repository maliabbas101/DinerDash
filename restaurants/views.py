from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.item import Item
from .models.category import Category
from .models.restaurant import Restaurant
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


# Create your views here.


class Index(View):
    def get(self, request):
        # request.session.clear()
        # print(request.GET)
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


class Cart(View):

    def get(self, request):
        ids = list(request.session.get('cart').keys())
        items = Item.get_item_by_ids(ids)
        return render(request, 'cart.html', {'items': items})


class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_index.html'

# class RestaurantView(View):
#     def get(self, request):
#         restaurants = Restaurant.get_all_restaurants()
#         categories = Category.get_all_categories()
#         restaurant_id = request.GET.get('restaurant')
#         print(restaurant_id)
#         if restaurant_id:
#             items = Item.get_items_by_category(restaurant_id)
#         else:
#             items = Item.get_all_items()
#         context = {
#             'restaurants': restaurants,
#             'items': items,
#             'categories': categories
#         }
#         return render(request, 'restaurants.html', context)
