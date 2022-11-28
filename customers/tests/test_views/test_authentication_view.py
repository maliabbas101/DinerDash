from django.test import TestCase, Client
from django.urls import reverse
from customers.models import Customer
from customers.tests.factories.customer import CustomerFactory, user_password
from faker import Faker
from customers.tests.factories.customer import GroupFactory
from restaurants.tests.factories import category, item, order, restaurant
from restaurants.models.item import Item
fake = Faker()


class TestAuthenticationViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.index_url = reverse('index')
        self.signup_url = reverse('signup')
        self.logout_url = reverse('logout')

        self.group = GroupFactory.create()

        self.customer = CustomerFactory.create(groups=(self.group,))
        # self.user = UserFactory.create(groups=(GroupFactory.create(),))
        self.category = category.CategoryFactory.create()
        self.restaurant = restaurant.RestaurantFactory.create(
            owner=self.customer)
        self.item = item.ItemFactory.create(restaurant=self.restaurant)
        self.item.categories.set((self.category,))
        self.item.save()

    def test_customer_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_customer_logout_get(self):
        response = self.client.get(self.logout_url)
        self.client.logout()
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/user/login')

    def test_customer_false_login_post(self):

        response = self.client.post(self.login_url, {
            'email': self.customer.email,
            'password': "123456"
        }, format='text/html')
        self.client.login(email=self.customer.email,
                          password="123456")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.customer.is_authenticated)

    def test_customer_login_post_when_cart_is_empty(self):

        response = self.client.post(self.login_url, {
            'email': self.customer.email,
            'password': user_password
        }, format='text/html')
        self.client.login(email=self.customer.email,
                          password=user_password)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.customer.is_authenticated)

    def test_customer_login_post_when_cart_is_not_empty(self):
        # response = self.client.post(self.index_url, {
        #     item: self.item
        # }, format='text/html')
        session = self.client.session
        session["cart"] = {}
        session["cart"].update({
            str(self.item.id): '1',

        })
        session.save()
        # if cart is not None:
        #     items_list = Item.get_item_by_ids(list(cart.keys()))
        # print(items_list)
        response = self.client.post(self.login_url, {
            'email': self.customer.email,
            'password': user_password
        }, format='text/html')
        self.client.login(email=self.customer.email,
                          password=user_password)
        self.assertEqual(response.status_code, 302)
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
        # customer = CustomerFactory()
        data = {
            'username': "aynlee_91",
            'email': fake.email(),
            'full_name': fake.name(),
            'password': "123456",
            'confirm_password': "123456",
            'phone_number': "03189989989",
            'groups': (self.group.id,)
        }
        self.common(data)

    def common(self, data):

        response = self.client.post(self.signup_url, data)
        customer = CustomerFactory.create(
            username=data['username'], email=data['email'], password=data['password'], phone_number=data['phone_number'])
        customer.save()
        customer.groups.set(data['groups'])
        customer.save()
        print(response)
        self.assertEqual(response.status_code, 302)

        customers = Customer.objects.all()
        self.assertEqual(customers.count(), 2)

    def test_signup_form_with_errors(self):
        # customer = CustomerFactory()
        data = {
            'username': "aynlee_91",
            'email': "example@gmail.com",
            'full_name': fake.name(),
            'password': "1233",
            'confirm_password': "1234",
            'phone_number': "03189989989",
            'groups': (self.group.id,)
        }

        data_second = {
            'username': "aynlee_91",
            'email': "example@gmail.com",
            'full_name': fake.name(),
            'password': "123345435",
            'confirm_password': "12345324",
            'phone_number': "03189989989",
            'groups': (self.group.id,)
        }

        self.common(data)
        self.common(data_second)
