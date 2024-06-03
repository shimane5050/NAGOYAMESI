from django.db import models
from django.core.validators import RegexValidator

class Shop(models.Model):
    name = models.CharField(max_length=20, verbose_name='店名')
    name_kana = models.CharField(max_length=20, verbose_name='店名かな')
    place = models.CharField(max_length=20, verbose_name='住所')
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    tel_number = models.CharField(validators=[tel_number_regex], max_length=15, default='114758758',verbose_name='電話番号')
    description = models.CharField(max_length=200, verbose_name='詳細')
    img = models.ImageField(blank=True, default='takosan.png')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '店舗情報'
        verbose_name_plural = '店舗情報'