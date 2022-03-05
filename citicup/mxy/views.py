from urllib import request, response
from django.db import connection
from django.shortcuts import render
from django import http
# Create your views here.
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView

class LoginAPIView(APIView):
    def get(self,request):
        # get apiview get params
        data = request.query_params
        print(data)
        id = data['id']
        password = data['password']
        cursor = connection.cursor()
        print(type(cursor))
        cursor.execute("select id,password from user where id=%s and password=%s",[id,password])
        print('exe')
        results = cursor.rowcount
        if results==1:
            return JsonResponse({"ifSuccess":True})  
        else:
            return JsonResponse({"ifSuccess":False})  

class GetAllGoodsAPIView(APIView):
    def get(self,request):
        cursor = connection.cursor()
        sql = "select id,goodName,goodType,goodCarbonCurrency,imagePath from good"
        cursor.execute(sql)
        connection.commit()
        results=cursor.fetchall()
        good_list = []
        for good in results:
            good_item={}
            good_item["id"]=good[0]
            good_item["goodName"]=good[1]
            good_item["goodType"]=good[2]
            good_item["goodCarbonCurrency"]=good[3]
            good_item["imagePath"]=good[4]
            good_list.append(good_item)
        cursor.close()
        res = JsonResponse.status_code
        if res==200:
            response = JsonResponse(good_list,safe=False)
            return response
        else:
            return JsonResponse({"status_code":res})

#获取商城中的商品分类
class GoodTypeAPIView(APIView):
    def get(self,request):
        cursor = connection.cursor()
        sql = "select id,goodTypeName from goodtype"
        cursor.execute(sql)
        connection.commit()
        results=cursor.fetchall()
        goodtype_list = []
        for goodtype in results:
            goodtype_item={}
            goodtype_item["id"]=goodtype[0]
            goodtype_item["goodTypeName"]=goodtype[1]
            goodtype_list.append(goodtype_item)
        cursor.close()
        res = JsonResponse.status_code
        if res==200:
            response = JsonResponse(goodtype_list,safe=False)
            return response
        else:
            return JsonResponse({"status_code":res})

#获取某个分类的所有商品
class CategorizedGoodAPIView(APIView):
    def get(self,request):
        data = request.query_params
        goodType=data['goodType']
        cursor = connection.cursor()
        cursor.execute("select id,goodName,goodType,goodCarbonCurrency,imagePath from good where goodType=%s",[goodType])
        connection.commit()
        results=cursor.fetchall()
        good_list = []
        for good in results:
            good_item={}
            good_item["id"]=good[0]
            good_item["goodName"]=good[1]
            good_item["goodType"]=good[2]
            good_item["goodCarbonCurrency"]=good[3]
            good_item["imagePath"]=good[4]
            good_list.append(good_item)
        cursor.close()
        res = JsonResponse.status_code
        if res==200:
            response = JsonResponse(good_list,safe=False)
            return response
        else:
            return JsonResponse({"status_code":res})


