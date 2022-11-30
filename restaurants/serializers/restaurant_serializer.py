from rest_framework import serializers
from restaurants.models.restaurant import Restaurant
from customers.serializers.customer_serializer import CustomerSerializer


class RestaurantSerializer(serializers.ModelSerializer):
    owner = CustomerSerializer()

    class Meta:
        model = Restaurant
        fields = "__all__"
