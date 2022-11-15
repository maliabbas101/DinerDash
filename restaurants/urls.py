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
    path('restaurants/<int:pk>/detail',
         views.restaurant.RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('restaurants/create/', views.restaurant.RestaurantCreateView.as_view(),
         name='restaurant_create'),
    path('films/<int:pk>/update/',
         views.restaurant.RestaurantUpdateView.as_view(), name='restaurant_update'),
    path('films/<int:pk>/delete/',
         views.restaurant.RestaurantDeleteView.as_view(), name='restaurant_delete'),


    # path('restaurants', views.RestaurantView.as_view(), name='restaurants'),
    # path('<int:pk>/', views.TestView.as_view(), name='test')

]
