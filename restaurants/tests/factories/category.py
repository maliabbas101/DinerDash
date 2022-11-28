from factory.django import DjangoModelFactory
from restaurants.models.category import Category

from . import restaurant
from faker import Faker
fake = Faker()


class CategoryFactory(DjangoModelFactory):

    class Meta:
        model = Category
        django_get_or_create = ('name',)

    name = fake.name()
