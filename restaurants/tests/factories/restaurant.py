from factory.django import DjangoModelFactory
from restaurants.models.restaurant import Restaurant
from customers.tests.factories.customer import CustomerFactory
from faker import Faker
fake = Faker()


class RestaurantFactory(DjangoModelFactory):

    class Meta:
        model = Restaurant
        django_get_or_create = ('name', 'owner')

    name = fake.name()
    location = "Lahore, Pakistan"
    contact = "+12125552368"
