# Generated by Django 4.1.3 on 2022-11-08 12:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('photo', models.ImageField(default='default_zgdqfn.png', upload_to='media/items/')),
                ('categories', models.ManyToManyField(default=1, to='restaurants.category')),
            ],
        ),
    ]
