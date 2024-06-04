# Generated by Django 5.0.6 on 2024-06-04 03:17

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='エリア名')),
            ],
            options={
                'verbose_name': 'エリア',
                'verbose_name_plural': 'エリア',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='カテゴリ名')),
            ],
            options={
                'verbose_name': 'カテゴリ',
                'verbose_name_plural': 'カテゴリ',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='価格帯名')),
            ],
            options={
                'verbose_name': '価格帯',
                'verbose_name_plural': '価格帯',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='店名')),
                ('name_kana', models.CharField(max_length=20, verbose_name='店名かな')),
                ('place', models.CharField(max_length=20, verbose_name='住所')),
                ('tel_number', models.CharField(default='114758758', max_length=15, validators=[django.core.validators.RegexValidator(message="Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed.", regex='^[0-9]+$')], verbose_name='電話番号')),
                ('open_time', models.TimeField(default='09:00', verbose_name='開店時間')),
                ('close_time', models.TimeField(default='22:00', verbose_name='閉店時間')),
                ('description', models.CharField(max_length=200, verbose_name='詳細')),
                ('img', models.ImageField(blank=True, default='takosan.png', upload_to='', verbose_name='画像')),
                ('closed_monday', models.BooleanField(default=False, verbose_name='月曜定休')),
                ('closed_tuesday', models.BooleanField(default=False, verbose_name='火曜定休')),
                ('closed_wednesday', models.BooleanField(default=False, verbose_name='水曜定休')),
                ('closed_thursday', models.BooleanField(default=False, verbose_name='木曜定休')),
                ('closed_friday', models.BooleanField(default=False, verbose_name='金曜定休')),
                ('closed_saturday', models.BooleanField(default=False, verbose_name='土曜定休')),
                ('closed_sunday', models.BooleanField(default=False, verbose_name='日曜定休')),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crud.area', verbose_name='エリア')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crud.category', verbose_name='カテゴリ')),
                ('price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crud.price', verbose_name='価格帯')),
            ],
            options={
                'verbose_name': '店舗情報',
                'verbose_name_plural': '店舗情報',
            },
        ),
    ]
