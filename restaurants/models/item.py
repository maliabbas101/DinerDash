from django.db import models
from django.core.validators import MinValueValidator
from .category import Category
from .restaurant import Restaurant


class Item(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0, validators=[
        MinValueValidator(1)
    ])
    photo = models.ImageField(upload_to='media/items/',
                              default='media/default_zgdqfn.png')

    categories = models.ManyToManyField(Category)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE)
    ordered_count = models.IntegerField(default=0)
    retired = models.BooleanField(default = False)

    class Meta:
        ordering = ['-ordered_count']

    def __str__(self):
        return self.title

    def increase_order_count(self, number):
        self.ordered_count += number
        return self

    @staticmethod
    def get_all_items():
        return Item.objects.all()

    @staticmethod
    def get_item_by_ids(ids):
        return Item.objects.filter(id__in=ids)

    @staticmethod
    def get_item_by_id(id):
        return Item.objects.filter(id=id)

    @staticmethod
    def get_items_by_category(category_id):
        if (category_id):
            return Item.objects.filter(categories=category_id)
        else:
            return Item.get_all_items()

    @staticmethod
    def get_items_by_restaurant(restaurant_id):
        if (restaurant_id):
            return Item.objects.filter(restaurant=restaurant_id)
        else:
            return Item.get_all_items()
