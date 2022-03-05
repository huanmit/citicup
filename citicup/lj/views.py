from pickle import FALSE
import re
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


class GoodAPIView(APIView):
    def get(self, request):
        data = request.query_params
        id = data.get('id', None)
        cursor = connection.cursor()
        sql = "select id,goodName,goodDescription,goodCarbonCurrency,goodLeft,imagePath from good where id = %s"
        cursor.execute(sql, [id])

        connection.commit()
        results = cursor.fetchall()
        result = results[0]

        response = []
        response.append({'id': result[0], 'goodName': result[1],
                         'goodDescription': result[2], 'goodCarbonCurrency': result[3],
                         'goodLeft': result[4], 'imagePath': result[5]})
        cursor.close()
        print(id)
        return JsonResponse(response, safe=False)


class UserPageAPIView(APIView):
    def get(self, request):
        data = request.query_params
        id = data.get('id', None)
        cursor = connection.cursor()
        sql = "select id,userName,phoneNumber,avatarPath,carbonCurrency,carbonCredit from user where id = %s"
        cursor.execute(sql, [id])

        connection.commit()
        results = cursor.fetchall()
        try:
            result_user = results[0]
        except:
            return JsonResponse({"status_code":500})

        sql = "select count(*) from plog where userId = %s"
        cursor.execute(sql, [id])
        connection.commit()
        results = cursor.fetchall()
        result_plog = results[0]


        sql = "select achievement.achievementName from achieves,achievement where userId =%s and achieves.achievementId = achievement.id ORDER BY achieveTime"
        cursor.execute(sql, [id])
        connection.commit()
        results = cursor.fetchall()
        try: 
            result_achieve = results[0]
        except: 
            result_achieve = [""]

        cursor.close()

        response = []
        response.append({'id': result_user[0], 'userName': result_user[1],
                         'phoneNumber': result_user[2], 'avatarPath': result_user[3],
                         'carbonCurrency': result_user[4], 'carbonCredit': result_user[5], \
                        'plogNum': result_plog[0],'lastAchievement':result_achieve[0]})

        print(id)
        return JsonResponse(response, safe=False)
