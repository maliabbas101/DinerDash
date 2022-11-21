from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from customers.models.customer import Customer


class Restaurant(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    contact = PhoneNumberField()


    def __str__(self):
        return self.name

    @staticmethod
    def get_all_restaurants():
        return Restaurant.objects.all()

    @staticmethod
    def get_restaurant_by_id(pid):
        return Restaurant.objects.filter(id__e=pid)
