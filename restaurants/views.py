from django.shortcuts import render
from django.http import HttpResponse
from .models.item import Item
from .models.category import Category

# Create your views here.


def index(request):
    category_id = request.GET.get('category')
    if category_id:
        items = Item.get_items_by_category(category_id)
    else:
        items = Item.get_all_items()

    categories = Category.get_all_categories()
    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'index.html', context)


def signup(request):
    return render(request, 'signup.html')
