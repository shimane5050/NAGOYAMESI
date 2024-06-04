from django.db import models
from django.core.validators import RegexValidator

# 価格帯モデル
class Price(models.Model):
     name = models.CharField(max_length=20, verbose_name='価格帯名')
 
     def __str__(self):
         return self.name
     
     class Meta:
        verbose_name = '価格帯'
        verbose_name_plural = '価格帯'

# エリアモデル
class Area(models.Model):
     name = models.CharField(max_length=20, verbose_name='エリア名')
 
     def __str__(self):
         return self.name
     
     class Meta:
        verbose_name = 'エリア'
        verbose_name_plural = 'エリア'


# カテゴリモデル
class Category(models.Model):
     name = models.CharField(max_length=20, verbose_name='カテゴリ名')
 
     def __str__(self):
         return self.name
     
     class Meta:
        verbose_name = 'カテゴリ'
        verbose_name_plural = 'カテゴリ'
         

# 店舗モデル
class Shop(models.Model):
    name = models.CharField(max_length=20, verbose_name='店名')
    name_kana = models.CharField(max_length=20, verbose_name='店名かな')
    place = models.CharField(max_length=20, verbose_name='住所')
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    tel_number = models.CharField(validators=[tel_number_regex], max_length=15, default='114758758',verbose_name='電話番号')
    open_time = models.TimeField(verbose_name="開店時間", default="09:00")
    close_time = models.TimeField(verbose_name="閉店時間", default="22:00")
    description = models.CharField(max_length=200, verbose_name='詳細')
    img = models.ImageField(blank=True, default='takosan.png', verbose_name='画像')
    closed_monday = models.BooleanField(verbose_name="月曜定休", default=False)
    closed_tuesday = models.BooleanField(verbose_name="火曜定休", default=False)
    closed_wednesday = models.BooleanField(verbose_name="水曜定休", default=False)
    closed_thursday = models.BooleanField(verbose_name="木曜定休", default=False)
    closed_friday = models.BooleanField(verbose_name="金曜定休", default=False)
    closed_saturday = models.BooleanField(verbose_name="土曜定休", default=False)
    closed_sunday = models.BooleanField(verbose_name="日曜定休", default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='カテゴリ')
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, verbose_name='エリア')
    price = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True, verbose_name='価格帯')


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '店舗情報'
        verbose_name_plural = '店舗情報'