from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('cart', views.Cart.as_view(), name='cart'),
    path('restaurants', views.RestaurantListView.as_view(), name='restaurants'),
    # path('restaurants', views.RestaurantView.as_view(), name='restaurants'),
    # path('<int:pk>/', views.TestView.as_view(), name='test')

]
