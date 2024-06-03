# Generated by Django 5.0.6 on 2024-06-03 09:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_shop_tel_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='tel_number',
            field=models.CharField(default='114758758', max_length=15, validators=[django.core.validators.RegexValidator(message="Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed.", regex='^[0-9]+$')], verbose_name='電話番号'),
        ),
    ]
