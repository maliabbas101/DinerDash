from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    path('', views.index.Index.as_view(), name='index'),
    path('cart', views.cart.Cart.as_view(), name='cart'),
    path('restaurants', views.restaurant.RestaurantListView.as_view(),
         name='restaurants'),
    path('checkout', login_required(
        views.checkout.CheckoutView.as_view(), login_url='login'), name='checkout'),
    path('orders', login_required(
        views.order_view.OrderView.as_view(), login_url='login'), name='orders'),

    # path('restaurants', views.RestaurantView.as_view(), name='restaurants'),
    # path('<int:pk>/', views.TestView.as_view(), name='test')

]
