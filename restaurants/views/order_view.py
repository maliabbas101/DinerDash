from django.shortcuts import render, redirect

from restaurants.models.order import Order
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from django.views import View

from customers.decorators import required_roles
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib import messages
import datetime

from restaurants.utils import *
from rest_framework import viewsets
from restaurants.serializers.order_serializer import OrderSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# @method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.get_all_orders()
    serializer_class = OrderSerializer

    # def common(self,request,pk):

    @method_decorator(required_roles(allowed_roles=['user']), name='dispatch')
    def create(self, request):
        return super(OrderViewSet, self).create(request)

    @method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
    def update(self, request, pk):
        return super(OrderViewSet, self).update(request, pk)

    @method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
    def partial_update(self, request, pk):
        return super(OrderViewSet, self).partial_update(request, pk)

    @method_decorator(required_roles(allowed_roles=[]), name='dispatch')
    def destroy(self, request, pk):
        return super(OrderViewSet, self).destroy(request, pk)


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
        if not (obj.restaurant in request.user.restaurant_set.all()):
            raise PermissionDenied
        return super(OrderDetailView, self).dispatch(request, *args, **kwargs)


@method_decorator(required_roles(allowed_roles=['user']), name='dispatch')
class OrderCreateView(OrderBaseView, CreateView):
    """View to create a new Order"""


@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class OrderUpdateView(OrderBaseView, UpdateView):
    """View to update a Order"""
    fields = ['status']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not (obj.restaurant in request.user.restaurant_set.all()):
            raise PermissionDenied
        if obj.status == "CM":
            messages.error(
                request, "Order is already completed can't change the status.")
            return redirect('orders_admin')
        return super(OrderUpdateView, self).dispatch(request, *args, **kwargs)


@method_decorator(required_roles(allowed_roles=['user']), name='dispatch')
class OrderDeleteView(OrderBaseView, DeleteView):
    success_url = reverse_lazy('orders_user')
    """View to delete a Order"""

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if not (obj.customer.email == str(request.user.email)):
            raise PermissionDenied
        request.session['cart'] = {}

        return super(OrderDeleteView, self).dispatch(request, *args, **kwargs)


@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class FilterOrderStatusView(View):
    def get(self, request, status):

        if status:
            orders = Order.get_orders_by_status(
                status, request.user.restaurant_set.all())
        else:
            orders = Order.get_all_orders()
        context = {
            'orders': orders
        }
        return render(request, 'order_status.html', context)


@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class ChangeOrderStatusView(View):
    def post(self, request):

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
        orderobject.datetime_updated = datetime.datetime.now()
        orderobject.placeOrder()
        return redirect('orders_admin')
