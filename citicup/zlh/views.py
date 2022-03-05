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


# 微信步数兑换 
# by_zlh
class UploadStepsAPIView(APIView):
    def post(self,request):
        data = request.data
        userId = data['userId']
        wx_steps = data['wx_steps']
        typeId = data['typeId']
        cursor = connection.cursor()
        cursor.execute("insert into Footprint(userId,carbonCurrency,typeId) values(%s,%s,%s)",[userId,wx_steps,typeId])
        cursor.execute("update User set carbonCurrency=carbonCurrency+%s where id=%s",[wx_steps,userId])

        response = JsonResponse({"status_code":JsonResponse.status_code})
        response['Access-Control-Allow-Origin']='*'
        print(response)
        return response