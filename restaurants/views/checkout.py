from django.shortcuts import redirect

from restaurants.models.item import Item

from restaurants.models.orders import Order
from customers.models.customer import Customer
from django.views import View


class CheckoutView(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        price = request.POST.get(('price'))
        customer = Customer.objects.get(id=request.user.id)
        cart = request.session.get('cart')
        items_list = Item.get_item_by_ids(list(cart.keys()))

        order = Order(customer=customer, price=price,
                      address=address, phone=phone)
        order.placeOrder()
        for item in items_list:
            order.set_items(item=item.id)

        order.placeOrder()
        request.session['cart'] = {}

        return redirect('cart')
