from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from restaurants.models.category import Category
from django.urls import reverse_lazy
from django.views import View
from customers.decorators import required_roles
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from restaurants.serializers.category_serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.get_all_categories()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CategoryBaseView(View):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('index')


@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class CategoryCreateView(CategoryBaseView, CreateView):
    """View to create a new Category"""
