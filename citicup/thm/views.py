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
        avatarPath = data['avatarPath']
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