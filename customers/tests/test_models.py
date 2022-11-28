from django.test import TestCase, Client
from django.urls import reverse
from customers.models import Customer
from customers.tests.factories.customer import CustomerFactory
from faker import Faker
fake = Faker()


class TestCustomerModel(TestCase):

    def setUp(self):
        self.customer = CustomerFactory()

    def test_register(self):
        updated_username = fake.name()
        self.customer.username = updated_username
        self.customer.register()
        self.assertEqual(self.customer.username, updated_username)

    def test_str(self):
        full_name = fake.name()
        self.customer.full_name = full_name
        self.assertEqual(self.customer.__str__(), full_name)
