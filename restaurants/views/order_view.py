from django.shortcuts import render

from restaurants.models.orders import Order
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from django.views import View

from customers.decorators import required_roles
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


class OrderView(View):
    def get(self, request):

        orders = Order.get_orders_by_customer(request.user.id)

        context = {
            'orders': orders
        }
        return render(request, 'orders.html', context)


class OrderBaseView(View):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('orders_admin')


class OrderListView(OrderBaseView, ListView):
    """
    """


class OrderDetailView(OrderBaseView, DetailView):
    """View to list the details from one Order.
    Use the 'Order' variable in the template to access
    the specific Order here and in the Views below"""
    # model = Order
    # template_name = 'Orders.html'


@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class OrderCreateView(OrderBaseView, CreateView):
    """View to create a new Order"""


@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class OrderUpdateView(OrderBaseView, UpdateView):
    """View to update a Order"""
    fields = ['status']


@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class OrderDeleteView(OrderBaseView, DeleteView):
    """View to delete a Order"""

class FilterOrderStatusView(View):
    def get(self,request,status):


        if status:
            orders = Order.get_orders_by_status(status)
        else:
            orders = Order.get_all_orders()
        context = {
            'orders': orders
        }
        return render(request, 'order_status.html',context)

