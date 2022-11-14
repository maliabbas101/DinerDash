from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.item import Item
from .models.category import Category
from django.views import View

# Create your views here.


class Index(View):
    def get(self, request):
        # request.session.clear()
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        category_id = request.GET.get('category')
        if category_id:
            items = Item.get_items_by_category(category_id)
        else:
            items = Item.get_all_items()

        categories = Category.get_all_categories()
        context = {
            'items': items,
            'categories': categories
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
