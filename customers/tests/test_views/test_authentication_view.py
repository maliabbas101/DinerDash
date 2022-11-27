from django.test import TestCase, Client
from django.urls import reverse
from customers.models import Customer
from faker import Faker
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user


class TestAuthenticationViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.fake = Faker()
        self.email = self.fake.email()
        self.username = self.fake.name()
        self.password = self.fake.password()
        self.customer = Customer.objects.create(
            email=self.email, username=self.username, password=self.password)
        # response = self.client.post(self.login_url)

    def test_customer_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_customer_login_post(self):
        response = self.client.post(self.login_url, {
            'email': self.customer.email,
            'password': '123456'
        })
        # print(response)
        self.assertEquals(response.status_code, 302)
        # self.assertRaisesMessage(
        #     response.message, "You have logged in successfully.")
