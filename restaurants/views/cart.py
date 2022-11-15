from django.shortcuts import render

from restaurants.models.item import Item
from django.views import View


class Cart(View):

    def get(self, request):
        ids = list(request.session.get('cart').keys())
        items = Item.get_item_by_ids(ids)
        return render(request, 'cart.html', {'items': items})
