import factory
from factory.django import DjangoModelFactory
from faker import Faker
from customers.models import Customer
import django.contrib.auth.models as auth_models
from django.contrib.auth.hashers import make_password

fake = Faker()
user_password = 'password'


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = auth_models.Group

    name = 'user'


class CustomerFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Customer
        django_get_or_create = ('username',)

    email = fake.email()
    username = fake.name()
    password = make_password(user_password)

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for group in extracted:
                self.groups.add(group)
