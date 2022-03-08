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


class RegisterAPIView(APIView):
    def post(self,request):
        data = request.data
        id = data['id']
        userName = data['userName']
        password = data['password']
        phoneNumber = data['phoneNumber']
        try:
            avatarPath = data['avatarPath']
        except:
            avatarPath = ""        
        carbonCurrency = 0
        carbonCredit = 0
        cursor = connection.cursor()
        print(data)
        cursor.execute("insert into user(id,userName,password,phoneNumber,avatarPath,carbonCurrency,carbonCredit) values(%s,%s,%s,%s,%s,%s,%s)",[id,userName,password,phoneNumber,avatarPath,carbonCurrency,carbonCredit])
        print(JsonResponse.status_code)
        response = JsonResponse(data)
        res = JsonResponse.status_code
        response['Access-Control-Allow-Origin']='*'
        print(type(res))
        response = JsonResponse({"status_code":res})
        return response

class SearchFootprintAPIView(APIView):
    def get(self,request):
        data = request.query_params
        user_id = data['user_id']
        time = data['time']
        print(user_id,time)

        cursor = connection.cursor()
        cursor.execute("select * from PlogType")
        results = cursor.fetchall()
        plogType = {}
        for each in results:
            id = str(each[0])
            name = each[1]
            plogType[id] = name

        cursor.execute("select * from footprint where userid=%s and foottime>=%s and foottime<=%s",[user_id,time+" 00:00:00",time+" 23:59:59"])
        results=cursor.fetchall()
        cnt = len(results) #记录个数
        list = []
        for each in results:
            dict = {}
            name = plogType[str(each[2])]
            dict["footprint_type_name"] = name
            dict["carbon_currency"] = each[3]
            dict["time"] = each[4]
            list.append(dict)

        response = JsonResponse(list,safe=False)
        return response

class SearchExchangeAPIView(APIView):
    def get(self,request):
        data = request.query_params
        user_id = data['user_id']
        time = data['time']

        cursor = connection.cursor()
        cursor.execute("select goodid from Exchanges where userid=%s and exchangetime>=%s and exchangetime<=%s",[user_id,time+" 00:00:00",time+" 23:59:59"])
        results = cursor.fetchall()
        # 没有记录
        if len(results) == 0:
            return JsonResponse({})
        # 有记录
        list = []
        for each in results:
            good_id = each[0]
            cursor.execute("select * from good where id=%s",[good_id])
            results = cursor.fetchall()
            good_name = results[0][1]
            good_price = results[0][-3] 
            dict = {"good_name":good_name, "good_price":good_price} 
            list.append(dict)

        response = JsonResponse(list,safe=False)
        return response

class LikeAPIView(APIView):
    def post(self,request):
        data = request.data
        user_id = data['user_id']
        plog_id = data['plog_id']

        cursor = connection.cursor()
        cursor.execute("insert into likes (userid,plogid) values(%s,%s)",[user_id,plog_id])
        
        response = JsonResponse(data)
        res = JsonResponse.status_code
        response['Access-Control-Allow-Origin']='*'
        response = JsonResponse({"status_code":res})
        return response 
