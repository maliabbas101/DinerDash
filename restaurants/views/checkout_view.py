from django.shortcuts import redirect

from restaurants.models.item import Item

from restaurants.models.order import Order
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
        order = Order.get_orders_by_customer_and_status(
            Customer.objects.get(id=request.user.id))
        if order.count() == 1:
            order = order[0]
            order.status = "OD"
            order.address = address
            order.phone = phone
            order.save()

        request.session['cart'] = {}
        messages.success(request, "Order placed successfully.")

        return redirect('cart')
