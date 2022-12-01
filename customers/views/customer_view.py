from rest_framework import viewsets
from customers.models.customer import Customer
from customers.serializers.customer_serializer import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
