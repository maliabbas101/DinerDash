from django.test import TestCase, Client
from django.urls import reverse
from restaurants.tests.factories.order import OrderFactory
from customers.tests.factories.customer import CustomerFactory
from customers.tests.factories.customer import GroupFactory
from restaurants.tests.factories.restaurant import RestaurantFactory
from faker import Faker
fake = Faker()


def fake_phone_number(fake):
    return f'+92 {fake.msisdn()[3:]}'


class TestCheckoutView(TestCase):

    def setUp(self):
        self.client = Client()
        self.checkout_url = reverse('checkout')
        self.cart_url = reverse('cart')
        # self.customer =
        self.user = CustomerFactory.create(groups=(GroupFactory.create(),))
        self.admin = CustomerFactory.create(
            groups=(GroupFactory.create(name='admin'),))
        self.order = OrderFactory(
            customer=self.user, restaurant=RestaurantFactory(owner=CustomerFactory()))

    def test_checkout_unathenticated_post(self):
        response = self.client.post(self.checkout_url, {
            'address': fake.address(),
            'phone': fake_phone_number(fake)
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user/login?next=/checkout')

        # self.client.login
    def test_checkout_admin_post(self):
        self.client.login(email=self.admin.email, password=self.admin.password)

        response = self.client.post(self.checkout_url, {
            'address': fake.address(),
            'phone': fake_phone_number(fake)
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user/login?next=/checkout')

    def test_checkout_user_post(self):
        self.client.login(email=self.user.email, password=self.user.password)

        response = self.client.post(self.checkout_url, {
            'address': fake.address(),
            'phone': fake_phone_number(fake)
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user/login?next=/checkout')
