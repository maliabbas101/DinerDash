from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator


class Customer(AbstractUser):
    username = models.CharField(
        _('Username'), max_length=32, blank=True, null=True, default='anonymoususer', unique=True)
    email = models.EmailField(_('Email'), max_length=255, unique=True)
    phone_number = PhoneNumberField(blank=True)
    full_name = models.CharField(max_length=50, default='User')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.full_name

    def register(self):
        self.save()
