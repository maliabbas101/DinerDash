from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from restaurants.models.restaurant import Restaurant
from django.urls import reverse_lazy
from django.views import View


class RestaurantBaseView(View):
    model = Restaurant
    fields = '__all__'
    success_url = reverse_lazy('Restaurants:all')


class RestaurantListView(RestaurantBaseView, ListView):
    """
    """


class RestaurantDetailView(RestaurantBaseView, DetailView):
    """View to list the details from one Restaurant.
    Use the 'Restaurant' variable in the template to access
    the specific Restaurant here and in the Views below"""
    # model = Restaurant
    # template_name = 'restaurants.html'


class RestaurantCreateView(RestaurantBaseView, CreateView):
    """View to create a new Restaurant"""


class RestaurantUpdateView(RestaurantBaseView, UpdateView):
    """View to update a Restaurant"""


class RestaurantDeleteView(RestaurantBaseView, DeleteView):
    """View to delete a Restaurant"""
