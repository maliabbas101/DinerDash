from django.test import TestCase, Client
from django.urls import reverse
from restaurants.tests.factories.order import OrderFactory
from customers.tests.factories.customer import CustomerFactory, user_password
from customers.tests.factories.customer import GroupFactory
from restaurants.tests.factories.restaurant import RestaurantFactory
from restaurants.tests.factories import category, item, restaurant
from faker import Faker
fake = Faker()


def fake_phone_number(fake):
    return f'+92 {fake.msisdn()[3:]}'


class TestCheckoutView(TestCase):

    def setUp(self):
        self.client = Client()
        self.checkout_url = reverse('checkout')
        self.cart_url = reverse('cart')

        self.user = CustomerFactory.create(groups=(GroupFactory.create(),))
        self.admin_group = GroupFactory.create(name="admin")
        self.admin = CustomerFactory.create(
            groups=(self.admin_group,))

        self.order = OrderFactory(
            customer=self.user, restaurant=RestaurantFactory(owner=CustomerFactory()))

        self.category = category.CategoryFactory.create()
        self.restaurant = restaurant.RestaurantFactory.create(
            owner=self.admin)
        self.item = item.ItemFactory.create(restaurant=self.restaurant)
        self.item.categories.set((self.category,))
        self.item.save()

        self.data = {
            'address': "Lahore,Pakistan",
            'phone': "031389832393"
        }

    def test_checkout_unathenticated_post(self):
        response = self.client.post(self.checkout_url, self.data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user/login?next=/checkout')

    def test_admin_can_checkout(self):
        self.client.login(email=self.admin.email, password=user_password)
        self.admin.groups.set((self.admin_group,))
        self.admin.save()

        response = self.client.post(self.checkout_url, self.data)

        self.assertEqual(response.status_code, 403)

    def test_checkout_user_cart(self):

        self.client.login(email=self.user.email,
                          password=user_password)

        response = self.client.post(self.checkout_url, self.data)

        session = self.client.session
        session["cart"] = {}
        session["cart"].update({
            str(self.item.id): 1,

        })
        session.save()

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/cart')

    def test_cart_get(self):
        response = self.client.get(self.cart_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    def test_cart_post(self):
        response = self.client.post(self.cart_url, {
            'item': self.item.id
        })
        self.assertEquals(response.status_code, 302)
        # self.assertRedirects('/cart')

    def test_cart_post_with_remove(self):
        response = self.client.post(self.cart_url, {
            'item': self.item.id,
            'remove': "True"
        })
        self.assertEquals(response.status_code, 302)
        # self.assertRedirects('/cart')

    def test_cart_post_with_authenticated_user(self):
        self.client.login(email=self.user.email,
                          password=user_password)

        response = self.client.post(self.cart_url, {
            'item': self.item.id,

        })
        self.assertEquals(response.status_code, 302)
        # self.assertRedirects('/cart')
