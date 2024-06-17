from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Avg
from .models import Shop, Review
from django.db.models import Q # get_queryset()用に追加
from django.contrib import messages # 検索結果のメッセージのため追加
import logging

class TopView(TemplateView):
    template_name = 'top.html'

class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'top.html'

class ShopListView(ListView):
    model = Shop
    template_name = 'crud/shop_list.html'

    # 1.全店舗データを取得する
    # 2.shopmodelのIDからレビューを全部引っ張ってくる
    # 3.スコアの平均値を出す
    # 4.店舗一覧に表示できるようにする

    def shop_review(request, shop_id):
        logging.debug('test')
        shop = Shop.objects.get(shop_id=shop_id)
        logging.debug(shop)
        scores = Review.objects.filter(shop=shop)
        average = scores.aggregate(Avg('score'))

        if average == None:
            average = 0
        average = round(average,2)

        return render(request, 'crud/shop_list.html', context={"average":average})
    
