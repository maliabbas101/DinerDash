from django.urls import path
from django.contrib.auth.decorators import login_required


from . import views
urlpatterns = [
    path('', views.index.Index.as_view(), name='index'),
    path('cart', views.cart.Cart.as_view(), name='cart'),
    path('checkout', login_required(
        views.checkout.CheckoutView.as_view(), login_url='login'), name='checkout'),
    path('orders', login_required(
        views.order_view.OrderView.as_view(), login_url='login'), name='orders'),

    path('restaurants', views.restaurant.RestaurantListView.as_view(),
         name='restaurants'),
    path('restaurants/<int:pk>/detail',
         views.restaurant.RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('restaurants/create/', views.restaurant.RestaurantCreateView.as_view(),
         name='restaurant_create'),
    path('restaurants/<int:pk>/update/',
         views.restaurant.RestaurantUpdateView.as_view(), name='restaurant_update'),
    path('restaurants/<int:pk>/delete/',
         views.restaurant.RestaurantDeleteView.as_view(), name='restaurant_delete'),

    path('items', views.item.ItemListView.as_view(),
         name='items'),
    path('items/<int:pk>/detail',
         views.item.ItemDetailView.as_view(), name='item_detail'),
    path('items/create/', views.item.ItemCreateView.as_view(),
         name='item_create'),
    path('items/<int:pk>/update/',
         views.item.ItemUpdateView.as_view(), name='item_update'),
    path('items/<int:pk>/delete/',
         views.item.ItemDeleteView.as_view(), name='item_delete'),


    # path('restaurants', views.RestaurantView.as_view(), name='restaurants'),
    # path('<int:pk>/', views.TestView.as_view(), name='test')

]
