from django.contrib import admin
from .models import Shop, Category, Area, Price

class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'place', 'category', 'area', 'price', 'tel_number')
    search_fields = ('name','name_kana',)

admin.site.register(Price, PriceAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Shop, ShopAdmin)

# Django管理サイト名変更
admin.site.site_header = 'NAGOYAMESI管理サイト'