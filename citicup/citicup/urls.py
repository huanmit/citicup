"""citicup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from thm.views import RegisterAPIView, SearchFootprintAPIView
from zlh.views import UploadStepsAPIView
from mxy.views import LoginAPIView,GetAllGoodsAPIView,GoodTypeAPIView,CategorizedGoodAPIView
from lj.views import GoodAPIView,UserPageAPIView,ReportAPIView

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # thm's part，记得打逗号！
    path('register/',RegisterAPIView.as_view()), #用户注册
    path('search_footprint/',SearchFootprintAPIView.as_view()),
    # zlh's part,记得打逗号！
    path('wxsteps_upload/',UploadStepsAPIView.as_view()),  #微信步数兑换

    # mxy's part,记得打逗号！
    path('login/',LoginAPIView.as_view()), #用户登录
    path('store/',GetAllGoodsAPIView.as_view()), #商城页面获取全部商品
    path('good_type/',GoodTypeAPIView.as_view()),#获取商城中的商品分类
    path('categorized_good/',CategorizedGoodAPIView.as_view()),#获取某个分类的所有商品

    # lj's part,记得打逗号！
    path('good/',GoodAPIView.as_view()), #商品详情页
    path('user_page/',UserPageAPIView.as_view()), #用户个人页面
    path('report/',ReportAPIView.as_view()), #举报
]