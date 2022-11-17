from django.urls import path
from customers.views.signup import Signup
from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [
    path('signup', views.signup.Signup.as_view(), name='signup'),
    path('login', views.authentication.Login.as_view(), name='login'),
    path('logout', views.authentication.logout_view, name='logout'),


    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
