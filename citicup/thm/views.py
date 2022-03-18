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
from thm.achievements import walker,master_walker,rider,master_rider,cutleryGuardian,traveler,master_traveler,chop_collector,clothes,clothes_lover
import thm.GarbageClassification as GC
import hashlib, time

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

class Achievements(APIView):
    def get(self,request):
        data = request.query_params
        user_id = data['user_id']

        # thm的两类成就,函数记得要import
        num_walker = walker(user_id) # 1.步行者
        num_master_walker = master_walker(user_id) # 6.步行达人
        # lj's
        num_rider = rider(user_id) # 2.骑行者，金银铜
        num_master_rider = master_rider(user_id) # 7.骑行达人，金银铜
        # mxy's
        num_cg = cutleryGuardian(user_id) # 3.餐具卫士，金银铜
        num_traveler = traveler(user_id) # 4.未来旅客，金银铜
        num_master_traveler = master_traveler(user_id) # 9.步未来旅行家，金银铜
        # zlh's
        num_chop = chop_collector(user_id) ##### 8.餐具收藏家 #####
        num_clothes = clothes(user_id) ##### 5.爱心使者 #####
        num_master_clothes = clothes_lover(user_id) ##### 10.爱心大使 #####



        return JsonResponse([num_walker,num_rider,num_cg,num_traveler,num_clothes,num_master_walker,num_master_rider,num_chop,num_master_traveler,num_master_clothes],safe=False)

class WebPlogType(APIView):
    def get(self, request):
        data = request.query_params
        id = data.get('id', None)
        cursor = connection.cursor()
        sql = "select id,typeName,typeCarbonCurrency from plogType where id =%s"
        cursor.execute(sql, [id])
        connection.commit()
        results = cursor.fetchall()
        try:
            result = results[0]
        except:
            return JsonResponse({"status_code":JsonResponse.status_code})

        response = []
        response.append({'id': result[0], 'typeName': result[1],'typeCarbonCurrency':result[2]})
        cursor.close()
        return JsonResponse(response, safe=False)

    def post(self,request):
        data = request.data
        type_name = data['type_name']
        type_coin = data['type_coin']
        if type_coin is None:
                 return JsonResponse({"error_tip":"汇率应为数字"}) 

        cursor = connection.cursor()
        cursor.execute("insert into plogtype (typename,typecarboncurrency) values(%s,%s)",[type_name,type_coin])
        
        res = JsonResponse.status_code
        response = JsonResponse({"status_code":res})
        return response 
    
    def put(self,request):
        data = request.data
        type_name = data['type_name']
        type_coin = data['type_coin'] 
        if type_coin is None:
                 return JsonResponse({"error_tip":"汇率应为数字"}) 

        id = data['id']
        cursor = connection.cursor()
 
        if type_name != "":
            cursor.execute("update plogtype set typename=%s where id=%s",[type_name,id])
        if type_coin != "":
            cursor.execute("update plogtype set typeCarbonCurrency=%s where id=%s",[type_coin,id])
        
        res = JsonResponse.status_code
        response = JsonResponse({"status_code":res})
        return response 
    
    def delete(self,request):
        data = request.query_params
        id = data.get('id')
        cursor = connection.cursor()
        cursor.execute("delete from plogtype where id=%s",[id])

        res = JsonResponse.status_code
        response = JsonResponse({"status_code":res})
        return response 

class WebGoodType(APIView):
    def get(self, request):
        data = request.query_params
        id = data.get('id')
        cursor = connection.cursor()
        sql = "select id,goodtypename from goodtype where id =%s"
        cursor.execute(sql, [id])
        connection.commit()
        results = cursor.fetchall()
        try:
            result = results[0]
        except:
            return JsonResponse({"status_code":JsonResponse.status_code})

        response = []
        response.append({'id': result[0], 'typeName': result[1]})
        cursor.close()
        return JsonResponse(response, safe=False)

    def post(self,request):
        data = request.data
        type_name = data['type_name']
        cursor = connection.cursor()
        cursor.execute("insert into goodtype (goodtypename) values(%s)",[type_name])
        
        res = JsonResponse.status_code
        response = JsonResponse({"status_code":res})
        return response 
    
    def put(self,request):
        data = request.data
        type_name = data['type_name']
        id = data['id']
        cursor = connection.cursor()
 
        if type_name != "":
            cursor.execute("update goodtype set goodtypename=%s where id=%s",[type_name,id])
        
        res = JsonResponse.status_code
        response = JsonResponse({"status_code":res})
        return response 
    
    def delete(self,request):
        data = request.query_params
        id = data.get('id')
        cursor = connection.cursor()
        cursor.execute("delete from goodtype where id=%s",[id])

        res = JsonResponse.status_code
        response = JsonResponse({"status_code":res})
        return response 

class WebRegister(APIView):
    def post(self,request):
        data = request.data
        id = data['id']
        userName = data['user_name']
        password = data['password']

        cursor = connection.cursor()

        
        cursor.execute("select id from adminuser where id=%s",[id]) 
        results = cursor.rowcount
        if results==1:
            return JsonResponse({"error_tip":"改用户id已被注册"})  
        
        cursor.execute("insert into adminuser(id,adminuserName,password) values(%s,%s,%s)",[id,userName,password])

        response = JsonResponse(data)
        res = JsonResponse.status_code
        response = JsonResponse({"status_code":res})
        return response

# 给 token 进行加密处理
def token_md5(user):
    ctime = str(time.time())  # 当前时间
    m = hashlib.md5(bytes(user, encoding="utf-8"))
    m.update(bytes(ctime, encoding="utf-8"))  # 加上时间戳
    return m.hexdigest()

class WebLogin(APIView):
    def post(self,request):
        data = request.data
        print(data)
        id = data['id']
        password = data['password']
        cursor = connection.cursor()
        cursor.execute("select id,password from adminuser where id=%s and password=%s",[id,password])
        results = cursor.rowcount
        if results==1:
            token = token_md5(id)
            return JsonResponse({"ifSuccess":True,"token":token})  
        else:
            return JsonResponse({"ifSuccess":False}) 

class WebGood(APIView):
    def post(self,request):
        data = request.data
        print(data)
        good_name = data["good_name"]
        print(good_name)
        good_type = data['good_type']
        good_description = data['good_description']
        good_carboncurrency = data['good_carboncurrency']
        good_left = data['good_left']
        image_path = data['image_path']

        cursor = connection.cursor()
        cursor.execute("insert into good (goodname,goodtype,gooddescription,goodcarboncurrency,goodleft,imagepath) values(%s,%s,%s,%s,%s,%s)",[good_name,good_type,good_description,good_carboncurrency,good_left,image_path])

        res = JsonResponse.status_code
        response = JsonResponse({"status_code":res})
        return response  

    def put(self,request):
        data = request.data
        good_name = data['good_name']
        good_type = data['good_type']
        good_description = data['good_description']
        good_carboncurrency = data['good_carboncurrency']
        good_left = data['good_left']
        image_path = data['image_path']
        id = data['id']
        
        cursor = connection.cursor()
        cursor.execute("update good set goodname=%s,goodtype=%s,gooddescription=%s,goodcarboncurrency=%s,goodleft=%s,imagepath=%s where id=%s",[good_name,good_type,good_description,good_carboncurrency,good_left,image_path,id])

        res = JsonResponse.status_code
        response = JsonResponse({"status_code":res})
        return response  


    def delete(self,request):
        data = request.query_params
        id = data.get('id')

        cursor = connection.cursor()
        cursor.execute("delete from good where id=%s",[id])

        res = JsonResponse.status_code
        response = JsonResponse({"status_code":res})
        return response  

class ProcessReport(APIView):
    def post(self,request):
        data = request.data
        report_id = data['report_id']
        admin_user = data['admin_user']
        result = data['result']
        result_detail = data['result_detail']

        cursor = connection.cursor()
        cursor.execute("insert into reportprocess (reportid,adminuser,result,resultdetail) values(%s,%s,%s,%s)",[report_id,admin_user,result,result_detail])
        
        cursor.execute("select plogid from reports where id=%s",[report_id])
        results = cursor.fetchall()
        plog_id = results[0][0] #int

        
        if int(result) == 1:
            cursor.execute("select userid,plogname from plog where id=%s",[plog_id])
            results = cursor.fetchall()
            user_id = results[0][0] #string
            plog_name = results[0][1]

            cursor.execute("update plog set plogname=%s,plogcontent=%s,imagepath=%s where id=%s",["这条帖子不见了噢","这条帖子不见了噢","",plog_id])
            cursor.execute("update user set carboncurrency=carboncurrency-100 where id=%s",[user_id])
            cursor.execute("insert into footprint (userid,plogtypeid,carboncurrency) values(%s,10,%s)",[user_id,-100])

        cursor.execute("update reports set status=1 where plogid=%s",[plog_id])
        res = JsonResponse.status_code
        response = JsonResponse({"status_code":res})
        return response 

class WebGetReport(APIView):
    def get(self,request):
        cursor = connection.cursor()
        cursor.execute("select * from reports where status=0")
        results = cursor.fetchall()
        list = []
        for each in results:
            dict = {}
            dict['report_id'] = each[0]
            dict['reporter'] = each[1]
            dict['report_content'] = each[4]
            dict['plog_id'] = each[2]
            cursor.execute("select * from plog where id=%s",[dict['plog_id']])
            plog = cursor.fetchall()[0]
            dict['plog_name'] = plog[5]
            dict['plog_content'] = plog[6]
            dict['poster'] = plog[1]
            list.append(dict)

        print(list)
 
        
        res = JsonResponse.status_code
        response = JsonResponse(list, safe = False)
        return response 

# 垃圾分类
# 发布Plog
class Garbage(APIView):
    def post(self,request):
        data = request.data
        file = request.FILES.get('file')
        #file_dir = os.path.join(os.getcwd(), 'upload_images')
        #file_path = os.path.join(file_dir, image_name)

        pred = GC.predict_img(file)
        print(pred)
        #print(img) # raw数据存入upload_files文件夹中
        return JsonResponse({'result':pred})