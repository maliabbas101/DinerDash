# Generated by Django 4.1.3 on 2022-11-11 09:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='display_picture',
            field=models.ImageField(default='media/person_default_ddlbql', upload_to='media/items/'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(blank=True, default='anonymoususer', max_length=32, null=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
