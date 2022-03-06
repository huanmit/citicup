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

        
