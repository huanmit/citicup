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
        coin = float(99)
        cursor.execute("insert into Plog(userID,plogTypeID,imagePath,plogName,plogContent) values(%s,%s,%s,%s,%s)",[userID,plogTypeID,imagePath,plogName,plogContent])
        cursor.execute("insert into footprint(userID,plogTypeID,carboncurrency) values(%s,%s,%s)",[userID,plogTypeID,coin])
        cursor.execute("update User set carbonCurrency=carbonCurrency+%s where id=%s",[coin,userID])
        response = JsonResponse({"status_code":JsonResponse.status_code})
        response['Access-Control-Allow-Origin']='*'
        print(response)
        return response

# 消息列表_comment
class CommentMessageAPIView(APIView):
    def get(self,request):
        data = request.query_params
        userID = data['userID']

        # 当用户点击查看我的消息列表时，首先根据用户id查找他发布过的帖子
        cursor = connection.cursor()
        cursor.execute("select id from Plog where userID=%s",[userID])
        results = cursor.fetchall() #该用户发布过的所有plog的id
        print("results:",results)
        print(len(results))

        if len(results) == 0 : #该用户未发布过plog
            response = JsonResponse({"status_code":500,"error_type":"您暂时没有消息噢！"})
        
        
        if len(results) > 0 :
            cursor.execute("select * from Comment where plogID in %s",[results])
            commentInfo = cursor.fetchall()
            print(commentInfo)
            print("info")
            comment_list = []
            for c in commentInfo:
                comment_item = {}
                comment_item["id"] = c[0]
                comment_item["plogID"] = c[1]
                comment_item["userID"] = c[2]
                comment_item["createTime"] = c[3]
                comment_item["commentContent"] = c[4]
                cursor.execute("select plogname from plog where id=%s",[c[1]])
                title = cursor.fetchall()[0][0]
                comment_item["plogTitle"] = title
                comment_list.append(comment_item)
     
        res = JsonResponse.status_code
        if res==200:
            response = JsonResponse(comment_list,safe=False)

        else:
            response = JsonResponse({"status_code":res})
        
        return response

# 消息列表_like
class LikeMessageAPIView(APIView):
    def get(self,request):
        data = request.query_params
        userID = data['userID']

        # 当用户点击查看我的消息列表时，首先根据用户id查找他发布过的帖子
        cursor = connection.cursor()
        cursor.execute("select id from Plog where userID=%s",[userID])
        results = cursor.fetchall() #该用户发布过的所有plog的id
        print("results:",results)

        if len(results) == 0 : #该用户未发布过plog
            response = JsonResponse({"status_code":500,"error_type":"您暂时没有消息噢！"})
        
        
        if len(results) > 0 :
            cursor.execute("select * from Likes where plogID in %s",[results])
            likeInfo = cursor.fetchall()
            like_list = []
            for l in likeInfo:
                like_item = {}
                like_item["userID"] = l[0]
                like_item["likeTime"] = l[1]
                like_item["plogID"] = l[2]
                cursor.execute("select plogname from plog where id=%s",[l[2]])
                title = cursor.fetchall()[0][0]
                like_item["plogTitle"] = title
                like_list.append(like_item)
            
        res = JsonResponse.status_code
        if res==200:
            response = JsonResponse(like_list,safe=False)

        else:
            response = JsonResponse({"status_code":res})
        
        return response

# 消息列表_report
class ReportMessageAPIView(APIView):
    def get(self,request):
        data = request.query_params
        userID = data['userID']

        # 当用户点击查看我的消息列表时，首先根据用户id查找他发布过的帖子
        cursor = connection.cursor()
        cursor.execute("select id from Plog where userID=%s",[userID])
        results = cursor.fetchall() #该用户发布过的所有plog的id
        print("results:",results)

        if len(results) == 0 : #该用户未发布过plog
            response = JsonResponse({"status_code":500,"error_type":"您暂时没有消息噢！"})
        
        
        if len(results) > 0 :
            cursor.execute("select * from Reports where plogID in %s",[results])
            reportInfo = cursor.fetchall()
                  
            report_list = []
            for r in reportInfo:
                report_item = {}
                report_item["id"] = r[0]
                report_item["userID"] = r[1]
                report_item["plogID"] = r[2]
                report_item["reportTime"] = r[3]
                report_item["reportContent"] = r[4]
                cursor.execute("select plogname from plog where id=%s",[r[2]])
                title = cursor.fetchall()[0][0]
                report_item["plogTitle"] = title
                report_list.append(report_item)
      
        res = JsonResponse.status_code
        if res==200:
            response = JsonResponse(report_list,safe=False)

        else:
            response = JsonResponse({"status_code":res})
        
        return response 
