from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from restaurants.models.item import Item
from django.urls import reverse_lazy
from django.views import View
from customers.decorators import required_roles
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from restaurants.serializers.item_serializer import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
  queryset = Item.get_all_items()
  serializer_class = ItemSerializer
class ItemBaseView(View):
    model = Item
    fields = ['title','description','price','categories','restaurant','photo','retired']
    success_url = reverse_lazy('items')


class ItemListView(ItemBaseView, ListView):
    """
    """


class ItemDetailView(ItemBaseView, DetailView):
    """View to list the details from one Item.
    Use the 'Item' variable in the template to access
    the specific Item here and in the Views below"""
    # model = Item
    # template_name = 'Items.html'


@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class ItemCreateView(ItemBaseView, CreateView):
    """View to create a new Item"""




@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class ItemUpdateView(ItemBaseView, UpdateView):
    """View to update a Item"""
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.email != obj.restaurant.owner.email:
            raise PermissionDenied
        return super(ItemUpdateView, self).dispatch(request, *args, **kwargs)


@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class ItemDeleteView(ItemBaseView, DeleteView):
    """View to delete a Item"""
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.email != obj.restaurant.owner.email:
            raise PermissionDenied
        return super(ItemDeleteView, self).dispatch(request, *args, **kwargs)
