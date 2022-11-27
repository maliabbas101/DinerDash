from django.test import SimpleTestCase
from django.urls import reverse, resolve
from customers.views import authentication, signup


class TestAuthenticationUrls(SimpleTestCase):
    def test_signup_url_is_resolved(self):
        url = reverse("signup")
        self.assertEquals(resolve(url).func.view_class, signup.Signup)

    def test_login_url_is_resolved(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func.view_class, authentication.Login)

    def test_logout_url_is_resolved(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func.view_class, authentication.Logout)
