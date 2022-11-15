from django.shortcuts import render

from restaurants.models.item import Item
from django.views import View
from customers.decorators import required_roles_for_cart
from django.utils.decorators import method_decorator


@method_decorator(required_roles_for_cart(allowed_roles=['user']), name='dispatch')
class Cart(View):

    # @required_roles(allowed_roles=['user'])
    def get(self, request):
        cart = request.session.get('cart')

        if not cart:
            request.session['cart'] = {}
        ids = list(request.session.get('cart').keys())
        items = Item.get_item_by_ids(ids)
        return render(request, 'cart.html', {'items': items})
