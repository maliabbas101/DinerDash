from rest_framework import serializers
from customers.models.customer import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["email", "username", "full_name", "phone_number", "groups"]
        depth = 1


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'username', 'email', 'password', 'username',
                  'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        customer = Customer.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return customer
