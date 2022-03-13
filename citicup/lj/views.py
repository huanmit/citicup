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
        sql = "select good.id,goodName,goodTypeName,goodDescription,goodCarbonCurrency,goodLeft,imagePath from good,goodtype where good.id =%s and good.goodType=goodtype.id"
        cursor.execute(sql, [id])
        connection.commit()
        results = cursor.fetchall()
        try:
            result = results[0]
        except:
            return JsonResponse({"status_code":JsonResponse.status_code})

        response = []
        response.append({'id': result[0], 'goodName': result[1],'goodType': result[2],
                         'goodDescription': result[3], 'goodCarbonCurrency': result[4],
                         'goodLeft': result[5], 'imagePath': result[6]})
        cursor.close()
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

        # 获得发帖数
        sql = "select count(*) from plog where userId = %s"
        cursor.execute(sql, [id])
        connection.commit()
        results = cursor.fetchall()
        result_plog = results[0]

        # 获得最近获得的成就
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
        return JsonResponse(response, safe=False)

class ReportAPIView(APIView):
    def post(self,request):
        cursor = connection.cursor()
        data = request.data
        userId = data['userId']

        # 确保有无提出举报的用户
        try: 
            cursor.execute("select id from user where id=%s",[userId])
            cursor.fetchall()[0]
        except:
             return JsonResponse({"status_code":500,"error_type":"找不到提出举报的用户"})

        # 查看有无被举报的帖子
        plogId = data['plogId']
        try: 
            cursor.execute("select id from plog where id=%s",[plogId])
            cursor.fetchall()[0]
        except:
             return JsonResponse({"status_code":500,"error_type":"找不到被举报的帖子"}) 

        reportContent = data['reportContent']
        cursor.execute("insert into reports(userId,plogId,reportContent) values(%s,%s,%s)",[userId,plogId,reportContent])
        connection.commit()
        response = JsonResponse({"status_code":JsonResponse.status_code})
        response['Access-Control-Allow-Origin']='*'
        return response 

class CommentAPIView(APIView):
    def post(self,request):
        cursor = connection.cursor()
        data = request.data

        # 查看有无该用户
        userId = data['userId']
        try: 
            cursor.execute("select id from user where id=%s",[userId])
            cursor.fetchall()[0]
        except:
             return JsonResponse({"status_code":500,"error_type":"找不到发出评论的用户"})

        # 查看有无该帖子
        plogId = data['plogId']
        try: 
            cursor.execute("select id from plog where id=%s",[plogId])
            cursor.fetchall()[0]
        except:
             return JsonResponse({"status_code":500,"error_type":"找不到被评论的帖子"}) 

        commentContent = data['commentContent']
        cursor.execute("insert into comment(userId,plogId,commentContent) values(%s,%s,%s)",[userId,plogId,commentContent])
        connection.commit()
        response = JsonResponse({"status_code":JsonResponse.status_code})
        response['Access-Control-Allow-Origin']='*'
        return response        

class UserPlogAPIView(APIView):
    def get(self, request):
        data = request.query_params
        id = data.get('userId', None)
        cursor = connection.cursor()
        sql = "select id,plogTypeId,imagePath,creatTime,plogName,plogContent from plog where userId = %s ORDER BY creatTime DESC"
        cursor.execute(sql, [id])
        connection.commit()
        results = cursor.fetchall()

        # 查看有无该用户
        try:
            results[0]
        except:
            return JsonResponse({"status_code":500})
           
        response = []
        for result in results:
            response.append({'id': result[0], 'plogTypeId': result[1],'imagePath': result[2],
                            'creatTime': result[3], 'plogName': result[4],
                            'plogContent': result[5]})
        return JsonResponse(response, safe=False)

        