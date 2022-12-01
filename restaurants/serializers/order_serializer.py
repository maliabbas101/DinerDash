from rest_framework import serializers
from restaurants.models.order import Order
from restaurants.serializers.item_serializer import ItemSerializer
from customers.serializers.customer_serializer import CustomerSerializer


class OrderSerializer(serializers.ModelSerializer):
    # items = ItemSerializer()
    customer = CustomerSerializer()
    # owner = CustomerSerializer()

    class Meta:
        model = Order
        fields = "__all__"
        depth = 1
