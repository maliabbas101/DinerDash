from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from restaurants.models.restaurant import Restaurant


class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_index.html'
