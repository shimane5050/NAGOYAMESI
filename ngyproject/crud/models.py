from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=20, verbose_name='店名')
    name_kana = models.CharField(max_length=20, verbose_name='店名かな')
    place = models.CharField(max_length=20, verbose_name='住所')
    description = models.CharField(max_length=200, verbose_name='詳細')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '店舗情報'
        verbose_name_plural = '店舗情報'