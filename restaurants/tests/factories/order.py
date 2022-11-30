from factory.django import DjangoModelFactory
from restaurants.models.order import Order

from . import restaurant
from faker import Faker
fake = Faker()


class OrderFactory(DjangoModelFactory):

    class Meta:
        model = Order
        django_get_or_create = ('restaurant',)

    price = "0"
