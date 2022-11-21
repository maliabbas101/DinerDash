from django.shortcuts import render,redirect

from restaurants.models.orders import Order
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from django.views import View

from customers.decorators import required_roles
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from restaurants.utils import *

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
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not(obj.restaurant in request.user.restaurant_set.all()):
            raise PermissionDenied
        return super(OrderDetailView, self).dispatch(request, *args, **kwargs)



@method_decorator(required_roles(allowed_roles=['user']), name='dispatch')
class OrderCreateView(OrderBaseView, CreateView):
    """View to create a new Order"""


@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class OrderUpdateView(OrderBaseView, UpdateView):
    """View to update a Order"""
    fields = ['status']
    print(fields)
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not(obj.restaurant in request.user.restaurant_set.all()):
            raise PermissionDenied
        if obj.status == "CM":
            messages.error(request,"Order is already completed can't change the status.")
            return redirect('orders_admin')
            # return super(OrderUpdateView, self).dispatch(request, *args, **kwargs
        return super(OrderUpdateView, self).dispatch(request, *args, **kwargs)




@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class OrderDeleteView(OrderBaseView, DeleteView):
    """View to delete a Order"""
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not(obj.restaurant in request.user.restaurant_set.all()):
            raise PermissionDenied
        return super(OrderDeleteView, self).dispatch(request, *args, **kwargs)

@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class FilterOrderStatusView(View):
    def get(self,request,status):


        if status:
            orders = Order.get_orders_by_status(status,request.user.restaurant_set.all())
        else:
            orders = Order.get_all_orders()
        context = {
            'orders': orders
        }
        return render(request, 'order_status.html',context)
@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class ChangeOrderStatusView(View):
    def post(self,request):

        cancel_id = request.POST.get('cancel')
        pay_id = request.POST.get('pay')
        complete_id = request.POST.get('complete')
        if cancel_id:
            orderobject = get_order(cancel_id)
            orderobject.status = "CN"
        elif pay_id:
            orderobject = get_order(pay_id)
            orderobject.status = "PI"
        else:
            orderobject = get_order(complete_id)
            orderobject.status = "CM"

        orderobject.placeOrder()
        return redirect('orders_admin')






        # return render(request, 'order_status.html',context)

