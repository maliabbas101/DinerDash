from django.db import models

from .item import Item
from customers.models.customer import Customer
import datetime


class Order(models.Model):
    items = models.ManyToManyField(Item)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.CharField(max_length=30)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)

    def placeOrder(self):
        self.save()

    def set_items(self, item):
        self.items.add(item)

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id)
