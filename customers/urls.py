from django.urls import path
from customers.views.signup import Signup
from .import views
urlpatterns = [
    path('signup', views.signup.Signup.as_view(), name='signup'),
    path('login', views.authentication.Login.as_view(), name='login'),
    path('logout', views.authentication.logout_view, name='logout')
]
