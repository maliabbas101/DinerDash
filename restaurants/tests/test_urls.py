from django.test import SimpleTestCase
from django.urls import reverse, resolve
from restaurants.views import checkout_view


class TestCheckoutUrls(SimpleTestCase):
    def test_checkout_is_resolved(self):
        url = reverse("checkout")
        self.assertEquals(resolve(url).func.view_class,
                          checkout_view.CheckoutView)
