from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import *


def index(request):
    # 获取导航菜单数据
    navigation=Navigation.objects.all()
    # 分类菜单数据
    # 三个表 category(一对多)    sub_menu(一对多)  sub_menu2
    categorys=Category.objects.all()
    for category in categorys:
        category.subs=category.submenu_set.all()
        for sub in category.subs:
           sub.subs2=sub.submenu2_set.all()
    # 轮播图数据
    banners = Banner.objects.all()
    return render(request,'index.heml',{'navigations':navigation,'banners':banners,'categorise':category})