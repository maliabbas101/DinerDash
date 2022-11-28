from factory.django import DjangoModelFactory
from faker import Faker
from customers.models import Customer

fake = Faker()


class CustomerFactory(DjangoModelFactory):

    class Meta:
        model = Customer
        django_get_or_create = ('username',)

    email = fake.email()
    username = fake.name()
    password = fake.password()
