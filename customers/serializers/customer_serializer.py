from rest_framework import serializers
from customers.models.customer import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["email", "username", "full_name", "phone_number", "groups"]
        depth = 1
