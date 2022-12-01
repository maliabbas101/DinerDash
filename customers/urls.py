from django.urls import path
from customers.views.signup import Signup
from django.contrib.auth import views as auth_views
from .import views
from rest_framework.routers import DefaultRouter
from .views.customer_view import CustomerViewSet

router = DefaultRouter()

router.register(r'customer-view-set', CustomerViewSet, basename="customer")


urlpatterns = [
    path('signup', views.signup.Signup.as_view(), name='signup'),
    path('login', views.authentication.Login.as_view(), name='login'),
    path('logout', views.authentication.Logout.as_view(), name='logout'),


    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
urlpatterns += router.urls
