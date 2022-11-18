from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Restaurant(models.Model):
    name = models.CharField(max_length=50,unique=True)
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
