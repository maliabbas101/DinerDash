from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Item)

admin.site.register(models.Category)

admin.site.register(models.Restaurant)

admin.site.register(models.Order)

admin.site.register(models.OrderItem)
