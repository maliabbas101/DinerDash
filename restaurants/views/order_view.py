from django.shortcuts import render

from restaurants.models.orders import Order

from django.views import View


class OrderView(View):
    def get(self, request):
        if request.user.groups.all()[0] == 'user':
            orders = Order.get_orders_by_customer(request.user.id)
        else:
            orders = Order.get_all_orders()

        context = {
            'orders': orders
        }
        return render(request, 'orders.html', context)
