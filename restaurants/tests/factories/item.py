from factory.django import DjangoModelFactory
from restaurants.models.item import Item

from . import restaurant
from faker import Faker
fake = Faker()


class ItemFactory(DjangoModelFactory):

    class Meta:
        model = Item
        django_get_or_create = ('title',)
    title = fake.name()
    description = fake.text()
    price = 1
