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
from mxy.achievements import cutleryGuardian,traveler,master_traveler

#用户登录
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

#获得商城中的商品列表
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

#首页获取全部帖子
class GetAllPlogAPIView(APIView):
    def get(self,request):
        cursor = connection.cursor()
        sql = "select id,userID,plogTypeID,imagePath,creatTime,plogName,plogContent from plog"
        cursor.execute(sql)
        connection.commit()
        results=cursor.fetchall()
        plog_list = []
        for plog in results:
            plog_item={}
            plog_item["id"]=plog[0]
            plog_item["userID"]=plog[1]
            plog_item["plogTypeID"]=plog[2]
            plog_item["imagePath"]=plog[3]
            plog_item["creatTime"]=plog[4]
            plog_item["plogName"]=plog[5]
            plog_item["plogContent"]=plog[6]
            plog_list.append(plog_item)
        cursor.close()
        res = JsonResponse.status_code
        if res==200:
            response = JsonResponse(plog_list,safe=False)
            return response
        else:
            return JsonResponse({"status_code":res})

 #首页获取所有帖子分类
class PlogTypeAPIView(APIView):
    def get(self,request):
        cursor = connection.cursor()
        sql = "select id,typeName,typeCarbonCurrency from plogtype"
        cursor.execute(sql)
        connection.commit()
        results=cursor.fetchall()
        plogtype_list = []
        for plogtype in results:
            plogtype_item={}
            plogtype_item["id"]=plogtype[0]
            plogtype_item["typeName"]=plogtype[1]
            plogtype_item["typeCarbonCurrency"]=plogtype[2]
            plogtype_list.append(plogtype_item)
        cursor.close()
        res = JsonResponse.status_code
        if res==200:
            response = JsonResponse(plogtype_list,safe=False)
            return response
        else:
            return JsonResponse({"status_code":res})

#获取某个分类的所有帖子
class CategorizedPlogAPIView(APIView):
    def get(self,request):
        data = request.query_params
        plogTypeID=data['plogTypeID']
        cursor = connection.cursor()
        cursor.execute("select id,userID,plogTypeID,imagePath,creatTime,plogName,plogContent from plog where plogTypeID=%s",[plogTypeID])
        connection.commit()
        results=cursor.fetchall()
        plog_list = []
        for plog in results:
            plog_item={}
            plog_item["id"]=plog[0]
            plog_item["userID"]=plog[1]
            plog_item["plogTypeID"]=plog[2]
            plog_item["imagePath"]=plog[3]
            plog_item["creatTime"]=plog[4]
            plog_item["plogName"]=plog[5]
            plog_item["plogContent"]=plog[6]
            plog_list.append(plog_item)
        cursor.close()
        res = JsonResponse.status_code
        if res==200:
            response = JsonResponse(plog_list,safe=False)
            return response
        else:
            return JsonResponse({"status_code":res})

#查看某条帖子详情页
class GetPlogDetailsAPIView(APIView):
    def get(self,request):
        data = request.query_params
        plogID=data['plogID']
        cursor = connection.cursor()
        cursor.execute("select count(plogID) from likes where plogID=%s",[plogID])
        likesNum=cursor.fetchone()
        cursor.execute("select id,userID,plogTypeID,imagePath,creatTime,plogName,plogContent from plog where id=%s",[plogID])
        plogDetail=cursor.fetchone()
        cursor.execute("select id,plogID,userID,creatTime,commentContent from comment where plogId=%s",[plogID])
        comment=cursor.fetchall()
        comment_list=[]      
        for commentContent in comment:
            comment_item={}
            comment_item["id"]=commentContent[0]
            comment_item["plogID"]=commentContent[1]
            comment_item["userID"]=commentContent[2]
            comment_item["creatTime"]=commentContent[3]
            comment_item["commentContent"]=commentContent[4]
            comment_list.append(comment_item)
        detail_list=[]
        detail_item={}
        detail_item["id"]= plogDetail[0]
        detail_item["userID"]= plogDetail[1]
        detail_item["plogTypeID"]= plogDetail[2]
        detail_item["imagePath"]=plogDetail[3]
        detail_item["creatTime"]=plogDetail[4]
        detail_item["plogName"]=plogDetail[5]
        detail_item["plogContent"]=plogDetail[6]
        detail_item["plogComment"]=comment_list
        detail_item["likesNum"]=likesNum
        detail_list.append(detail_item)
        cursor.close()
        res = JsonResponse.status_code
        if res==200:
            response = JsonResponse(detail_list,safe=False)
            return response
        else:
            return JsonResponse({"status_code":res}) 
#成就
class AchievementsM(APIView):
    def get(self,request):
        data = request.query_params
        user_id = data['user_id']

        # mxy的成就,函数记得要import
        num_cutleryGuardian = cutleryGuardian(user_id) # 餐具卫士
        num_traveler = traveler(user_id) # 未来旅客
        num_master_traveler = master_traveler(user_id) # 未来旅行家


        return JsonResponse([num_cutleryGuardian,num_traveler,num_master_traveler],safe=False)
        #return JsonResponse([0,0,0,0,0,0,0,0,0,0],safe = False)