from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from restaurants.models.restaurant import Restaurant
from customers.models.customer import Customer
from django.urls import reverse_lazy
from django.views import View
from customers.decorators import required_roles
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.shortcuts import render,redirect


class RestaurantBaseView(View):
    model = Restaurant
    fields = '__all__'
    success_url = reverse_lazy('restaurants')


class RestaurantListView(RestaurantBaseView, ListView):
    """
    """


class RestaurantDetailView(RestaurantBaseView, DetailView):
    """View to list the details from one Restaurant.
    Use the 'Restaurant' variable in the template to access
    the specific Restaurant here and in the Views below"""
    # model = Restaurant
    # template_name = 'restaurants.html'


@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class RestaurantCreateView(RestaurantBaseView, CreateView):
    """View to create a new Restaurant"""
    fields = ['name','location','contact']
    def post(self,request):
        name = request.POST.get('name')
        location = request.POST.get('location')
        contact = request.POST.get('contact')
        owner_id = request.POST.get('owner')

        owner = Customer.objects.filter(id=owner_id)[0]
        restaurant = Restaurant(name = name, location= location,contact=contact, owner=owner)
        restaurant.save()
        return redirect('restaurants')


@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class RestaurantUpdateView(RestaurantBaseView, UpdateView):
    """View to update a Restaurant"""

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.email != obj.owner.email:
            raise PermissionDenied
        return super(RestaurantUpdateView, self).dispatch(request, *args, **kwargs)


@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class RestaurantDeleteView(RestaurantBaseView, DeleteView):
    """View to delete a Restaurant"""
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.email != obj.owner.email:
            raise PermissionDenied
        return super(RestaurantDeleteView, self).dispatch(request, *args, **kwargs)
