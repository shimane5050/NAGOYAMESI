# Generated by Django 5.0.6 on 2024-06-03 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('name_kana', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]