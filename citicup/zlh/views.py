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
from zlh.WXBizDataCrypt import WXBizDataCrypt




# 微信步数兑换 
# by_zlh
class UploadStepsAPIView(APIView):
    def post(self,request):
        data = request.data
        #data = json.loads(request.get_data().decode('utf-8'))

        appId = data['appId']
        sessionKey = data['sessionKey']
        encryptedData = data['encryptedData']
        iv = data['iv']
        pc = WXBizDataCrypt(appId,sessionKey)
        wxSteps = pc.decrypt(encryptedData,iv)
        wxSteps = wxSteps['stepInfoList'][-1]['step']
        print(wxSteps)

        userID = data['userID']
        plogTypeID = data['plogTypeID']
        cursor = connection.cursor()
        cursor.execute("insert into Footprint(userID,carbonCurrency,plogTypeID) values(%s,%s,%s)",[userID,wxSteps,plogTypeID])
        cursor.execute("update User set carbonCurrency=carbonCurrency+%s where id=%s",[wxSteps,userID])

        response = JsonResponse({"status_code":JsonResponse.status_code})
        response['Access-Control-Allow-Origin']='*'
        print(response)
        return response

#  兑换商品
class ExchangeGoodAPIView(APIView):
    def  post(self,request):
        data = request.data
        
        userID = data['userID']
        goodID = data['goodID']
        goodCarbonCurrency = data['goodCarbonCurrency']

        cursor = connection.cursor()
        cursor.execute("insert into Exchanges (userID, goodID) values (%s,%s)",[userID,goodID])
       
        cursor.execute("select carbonCurrency from User where id=%s",[userID])
        result = cursor.fetchall()
        result = result[0][0]
        print(result)
        # 碳币充足时
        if result >= goodCarbonCurrency:
            cursor.execute("update User set carbonCurrency=carbonCurrency-%s where id=%s",[goodCarbonCurrency,userID])
            response = JsonResponse({"status_code":JsonResponse.status_code})
            response['Access-Control-Allow-Origin']='*'
            print(response)
        

        #碳币不足时
        if result < goodCarbonCurrency:
            response = JsonResponse({"status_code":500,"error_type":"您的碳币不足！"})

        return response

        
        


# 发布Plog
class PostPlogAPIView(APIView):
    def  post(self,request):
        data = request.data

        userID = data['userID']
        plogTypeID = data['plogTypeID']
        imagePath = data['imagePath']
        plogName = data['plogName']
        plogContent = data['plogContent']

        cursor = connection.cursor()
        cursor.execute("insert into Plog(userID,plogTypeID,imagePath,plogName,plogContent) values(%s,%s,%s,%s,%s)",[userID,plogTypeID,imagePath,plogName,plogContent])
        
        response = JsonResponse({"status_code":JsonResponse.status_code})
        response['Access-Control-Allow-Origin']='*'
        print(response)
        return response

        
