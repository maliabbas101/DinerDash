from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    contact = PhoneNumberField()

    def __str__(self):
        return self.name
