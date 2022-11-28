from django.test import TestCase, Client
from django.urls import reverse
from customers.models import Customer
from faker import Faker
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user
from customers.tests.factories.customer import CustomerFactory


class TestAuthenticationViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.signup_url = reverse('signup')
        self.customer = CustomerFactory()

    def test_customer_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_customer_login_post(self):
        response = self.client.post(self.login_url, {
            'email': self.customer.email,
            'password': self.customer.password
        })
        self.assertEquals(response.status_code, 302)
        self.assertTrue(self.customer.is_authenticated)

    def test_customer_signup_get(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_customer_signup_get(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        customer = CustomerFactory()
        response = self.client.post(self.signup_url, data={
            'username': customer.username,
            'email': customer.email,
            'password': customer.password,
        })
        self.assertEqual(response.status_code, 302)

        customers = Customer.objects.all()
        self.assertEqual(customers.count(), 1)
