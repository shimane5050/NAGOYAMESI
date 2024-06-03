from django.contrib import admin
from .models import Shop, Category

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'place')
    search_fields = ('name','name_kana',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)

# Django管理サイト名変更
admin.site.site_header = 'NAGOYAMESI管理サイト'