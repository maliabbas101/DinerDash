from django.db import models

from .item import Item
from customers.models.customer import Customer
from restaurants.models.restaurant import Restaurant
import datetime


class Order(models.Model):
    STATUS_ORDERED = "OD"
    STATUS_PAID = "PI"
    STATUS_CANCELLED = "CN"
    STATUS_COMPLETED = "CM"
    STATUS_COMPLETED = "CM"
    STATUS_PENDING = "PN"

    STATUS_CHOICES = [
        (STATUS_ORDERED, "Ordered"),
        (STATUS_PAID, "Paid"),
        (STATUS_CANCELLED, "Cancelled"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_PENDING, "Pending"),
    ]
    items = models.ManyToManyField(Item)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.CharField(max_length=30)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,default=34)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    datetime_updated = models.DateTimeField(null=True,blank = True)
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=STATUS_PENDING)

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
    def get_orders_by_status(status,restaurants):
        return Order.objects.filter(status=status, restaurant__in=restaurants)

    @staticmethod
    def get_all_orders():
        return Order.objects.all()

    @staticmethod
    def get_order_by_id(id):
        return Order.objects.filter(id=id)
