from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator


class Customer(models.Model):
    username = models.CharField(
        max_length=32, blank=True, null=True, validators=[MinLengthValidator(2)])
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.full_name
