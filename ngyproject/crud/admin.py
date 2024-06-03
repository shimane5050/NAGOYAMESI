from django.contrib import admin
from .models import Shop

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'place')
    search_fields = ('name','name_kana')

admin.site.register(Shop, ShopAdmin)

# Django管理サイト名変更
admin.site.site_header = 'NAGOYAMESI管理サイト'