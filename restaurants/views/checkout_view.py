from django.shortcuts import redirect

from restaurants.models.item import Item

from restaurants.models.orders import Order
from customers.models.customer import Customer
from django.views import View
from customers.decorators import required_roles_for_cart
from django.utils.decorators import method_decorator
from django.contrib import messages
from restaurants.models.restaurant import Restaurant

@method_decorator(required_roles_for_cart(allowed_roles=['user']), name='dispatch')
class CheckoutView(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        price = request.POST.get(('price'))
        customer = Customer.objects.get(id=request.user.id)
        cart = request.session.get('cart')
        items_list = Item.get_item_by_ids(list(cart.keys()))
        items_quantity = list(cart.values())
        restaurant = request.POST.get('restaurant')
        restaurant_ord = Restaurant.objects.filter(name=restaurant).first()

        order = Order(customer=customer, price=price, restaurant=restaurant_ord,
                      address=address, phone=phone)
        order.placeOrder()
        for item, item_quantity in zip(items_list, items_quantity):
            order.set_items(item.id, item_quantity)

        order.placeOrder()
        request.session['cart'] = {}
        messages.success(request,"Order placed successfully.")

        return redirect('cart')
