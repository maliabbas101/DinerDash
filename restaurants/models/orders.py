from django.db import models

from .item import Item
from customers.models.customer import Customer
import datetime


class Order(models.Model):
    STATUS_ORDERED = "OD"
    STATUS_PAID = "PI"
    STATUS_CANCELLED = "CN"
    STATUS_COMPLETED = "CM"
    STATUS_CHOICES = [
        (STATUS_ORDERED, "Ordered"),
        (STATUS_PAID, "Paid"),
        (STATUS_CANCELLED, "Cancelled"),
        (STATUS_COMPLETED, "Completed"),
    ]
    items = models.ManyToManyField(Item)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.CharField(max_length=30)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=STATUS_ORDERED)

    def placeOrder(self):
        self.save()

    def set_items(self, item, item_quantity):
        ordered_item = Item.objects.get(id=item)
        item = Item.increase_order_count(ordered_item, item_quantity)
        item.save()
        self.items.add(item)

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id)

    @staticmethod
    def get_orders_by_status(status):
        return Order.objects.filter(status=status)

    @staticmethod
    def get_all_orders():
        return Order.objects.all()
