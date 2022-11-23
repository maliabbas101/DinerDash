from django.shortcuts import render, redirect

from restaurants.models.item import Item
from django.views import View
from customers.decorators import required_roles_for_cart
from django.utils.decorators import method_decorator
from restaurants.utils import cart_quantity, creating_pending_orders
from django.contrib import messages
from customers.models.customer import Customer


@method_decorator(required_roles_for_cart(allowed_roles=['user']), name='dispatch')
class Cart(View):

    def get(self, request):
        cart = request.session.get('cart')

        if not cart:
            request.session['cart'] = {}
        ids = request.session.get('cart').keys()
        items = Item.get_item_by_ids(ids)
        return render(request, 'cart.html', {'items': items})

    def post(self, request):
        item = request.POST.get('item')
        item_ord = Item.get_item_by_id(item)[0]

        cart = request.session.get('cart')
        remove = request.POST.get('remove')

        request.session['cart'] = cart_quantity(item, cart, remove)

        if request.user.is_authenticated:
            cart = request.session.get('cart')
            customer = Customer.objects.filter(id=request.user.id)[0]

            creating_pending_orders(cart, customer, remove, item_ord, item)

        if remove:
            messages.error(request, "Item removed from Cart.")
        else:
            messages.success(request, "Item added to Cart.")
        return redirect('cart')
