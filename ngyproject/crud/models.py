from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils import timezone


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


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            username=username, 
            email=self.normalize_email(email),
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'ユーザー情報'
        verbose_name_plural = 'ユーザー情報'

SCORE_CHOICES = [
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
]

class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=False, verbose_name='店舗', default='1')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=20, blank=False)
    comment = models.TextField(verbose_name='レビューコメント', blank=False)
    score = models.PositiveSmallIntegerField(verbose_name='レビュースコア', choices=SCORE_CHOICES, default='3')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('shop', 'user')

    def __str__(self):
        return str(self.title)

    def get_percent(self):
        percent = round(self.score / 5 * 100)
        return percent



