# Generated by Django 5.0.6 on 2024-06-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=20, verbose_name='店名'),
        ),
    ]
