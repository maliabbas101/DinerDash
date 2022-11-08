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
        Restaurant, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
