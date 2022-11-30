from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from .views.item_view import ItemViewSet
from .views.restaurant_view import RestaurantViewSet
router = DefaultRouter()
router.register(r'item-view-set', ItemViewSet, basename="item")
router.register(r'restaurant-view-set', RestaurantViewSet, basename="item")

urlpatterns = [
    path('', views.index_view.Index.as_view(), name='index'),
    path('cart', views.cart_view.Cart.as_view(), name='cart'),
    path('checkout', login_required(
        views.checkout_view.CheckoutView.as_view(), login_url='login'), name='checkout'),
    path('orders_user', login_required(
        views.order_view.OrderView.as_view(), login_url='login'), name='orders_user'),

    path('restaurants', views.restaurant_view.RestaurantListView.as_view(),
         name='restaurants'),
    path('restaurants/<int:pk>/detail',
         views.restaurant_view.RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('restaurants/create/', views.restaurant_view.RestaurantCreateView.as_view(),
         name='restaurant_create'),
    path('restaurants/<int:pk>/update/',
         views.restaurant_view.RestaurantUpdateView.as_view(), name='restaurant_update'),
    path('restaurants/<int:pk>/delete/',
         views.restaurant_view.RestaurantDeleteView.as_view(), name='restaurant_delete'),

    path('items', views.item_view.ItemListView.as_view(),
         name='items'),
    path('items/<int:pk>/detail',
         views.item_view.ItemDetailView.as_view(), name='item_detail'),
    path('items/create/', views.item_view.ItemCreateView.as_view(),
         name='item_create'),
    path('items/<int:pk>/update/',
         views.item_view.ItemUpdateView.as_view(), name='item_update'),
    path('items/<int:pk>/delete/',
         views.item_view.ItemDeleteView.as_view(), name='item_delete'),

    path('orders', login_required(views.order_view.OrderListView.as_view(), login_url='login'),
         name='orders_admin'),
    path('orders/<int:pk>/detail',
         login_required(views.order_view.OrderDetailView.as_view(), login_url='login'), name='order_detail'),

    path('orders/create/', login_required(views.order_view.OrderCreateView.as_view(), login_url='login'),
         name='order_create'),
    path('orders/<int:pk>/update/',
         login_required(views.order_view.OrderUpdateView.as_view(), login_url='login'), name='order_update'),
    path('orders/<int:pk>/delete/',
         login_required(views.order_view.OrderDeleteView.as_view(), login_url='login'), name='order_delete'),

    path('orders/create/', login_required(views.order_view.OrderCreateView.as_view(), login_url='login'),
         name='order_create'),

    path('orders/<str:status>/filter/',
         login_required(views.order_view.FilterOrderStatusView.as_view(), login_url='login'), name='order_status'),

    path('change_order_status', login_required(views.order_view.ChangeOrderStatusView.as_view(), login_url='login'),
         name='change_order_status'),

    path('categories/create/', login_required(views.category_view.CategoryCreateView.as_view(), login_url='login'),
         name='category_create'),

]
urlpatterns += router.urls
