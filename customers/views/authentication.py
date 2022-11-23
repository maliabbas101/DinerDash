from django.shortcuts import render, redirect

from customers.forms import CustomerLoginForm
from django.http import HttpResponse
# Create your views here.
from django.views import View
from restaurants.models.order import Order
from restaurants.models.order_items import OrderItem
from customers.models.customer import Customer
from restaurants.models.restaurant import Restaurant
from restaurants.models.item import Item
from restaurants.utils import cart_quantity


from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


from django.contrib import messages

from django.utils.decorators import method_decorator
from customers.decorators import persist_session_vars


# @method_decorator(persist_session_vars(['carts']), name='dispatch')

class Login(View):
    context = {
        'errors': '',
        'form': CustomerLoginForm()
    }

    def get(self, request):

        return render(request, 'login.html', self.context)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            current_customer = Customer.objects.get(id=request.user.id)

            # if cart is not None:
            if request.user.groups.all()[0].name != "admin":

                order = Order.get_orders_by_customer_and_status(
                    current_customer)

                if order.count() < 1:
                    cart = request.session.get('cart')

                    if cart is not None:
                        items_list = Item.get_item_by_ids(list(cart.keys()))
                        items_quantity = list(cart.values())
                        restaurant = items_list[0].restaurant
                        order_pending = Order(customer=Customer.objects.get(
                            id=request.user.id), price="0", restaurant=restaurant)
                        order_pending.save()

                        for item_cart, item_quantity in zip(items_list, items_quantity):
                            order_item = OrderItem(
                                item=item_cart, order=order_pending, item_price=item_cart.price, item_quantity=item_quantity)
                            order_pending.price = int(
                                order_pending.price) + item_cart.price
                            order_pending.save()
                            order_item.save()
                    else:
                        order_pending = Order(customer=Customer.objects.get(id=request.user.id), price="0"
                                              )
                        order_pending.save()
                else:

                    cart = request.session['cart'] = {}
                    pending_orders = Order.get_orders_by_customer_and_status(
                        current_customer)
                    order_items = OrderItem.get_orders_by_ids(pending_orders)
                    items_list = []
                    items_quantity = []

                    for items in order_items:
                        items_list.append(items.item)
                        items_quantity.append(items.item_quantity)

                    for item, item_quantity in zip(items_list, items_quantity):
                        cart[item.id] = item_quantity

            messages.success(request, "You have logged in successfully.")
            return redirect('index')

        else:
            messages.error(request, "Invalid email or password.")

            return redirect('login')

# @method_decorator(persist_session_vars(['cart']), name='dispatch')


class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have logged out successfully.")

        return redirect('login')
