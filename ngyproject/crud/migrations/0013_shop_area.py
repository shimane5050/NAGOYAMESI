# Generated by Django 5.0.6 on 2024-06-03 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0012_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crud.area'),
        ),
    ]
