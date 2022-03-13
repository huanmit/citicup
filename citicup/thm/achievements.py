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

# 1.步行者，金银铜
def walker(user_id:str):
    res = 0
    if bronze_walker(user_id) == True:
        res += 1
    if silver_walker(user_id) == True:
        res += 1
    if gold_walker(user_id) == True:
        res += 1
    return res

# 6.步行达人，金银铜
def master_walker(user_id:str):
    res = 0
    if bronze_master_walker(user_id) == True:
        res += 1
    if silver_master_walker(user_id) == True:
        res += 1
    if gold_master_walker(user_id) == True:
        res += 1
    return res

# 单次步行2w步,后期注意换算的问题
def bronze_walker(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=1 and userid=%s",[user_id])
    results = cursor.fetchall()

    for each in results:
        if each[0] >= 10000: # 建模后要更改
            return True
    return False

# 累计上传步行10天
def silver_walker(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=1 and userid=%s",[user_id])
    results = cursor.fetchall()
    cnt = 0
    for each in results:
        if each[0] >= 10000:
            cnt += 1
    if cnt >= 10:
        return True
    return False

# 累计上传步行30天
def gold_walker(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=1 and userid=%s",[user_id])
    results = cursor.fetchall()
    cnt = 0
    for each in results:
        if each[0] >= 10000:
            cnt += 1
    if cnt >= 30:
        return True
    return False

# 100w步
def bronze_master_walker(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=1 and userid=%s",[user_id])
    results = cursor.fetchall()
    sum = 0
    for each in results:
        sum += each[0]
    if sum >= 1000000:
        return True
    return False

# 500w步
def silver_master_walker(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=1 and userid=%s",[user_id])
    results = cursor.fetchall()
    sum = 0
    for each in results:
        sum += each[0]
    if sum >= 5000000:
        return True
    return False

# 1000w步
def gold_master_walker(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=1 and userid=%s",[user_id])
    results = cursor.fetchall()
    sum = 0
    for each in results:
        sum += each[0]
    if sum >= 10000000:
        return True
    return False

# lj's part
# 2.骑行者，金银铜
def rider(user_id:str):
    res = 0
    res = bronze_rider(user_id) + silver_or_gold_rider(user_id)
    return res

# 7.骑行达人，金银铜
def master_rider(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=2 and userid=%s",[user_id])
    results = cursor.fetchall()
    sum = 0
    for each in results:
        sum += each[0]
    if sum >= 1000000:
        return 3
    else:
        if sum >= 500000:
            return 2
        else:
            if sum >= 100000:  
                return 1 
    return 0    

# 单次骑行3km,后期注意换算的问题
def bronze_rider(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=2 and userid=%s",[user_id])
    results = cursor.fetchall()

    for each in results:
        if each[0] >= 3000: # 建模后要更改
            return 1
    return 0   

# 累计上传骑行数据10天或者30天以上
def silver_or_gold_rider(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=2 and userid=%s",[user_id])
    results = cursor.fetchall()
    cnt = 0
    for each in results:
        if each[0] >= 3000:
            cnt += 1
    if cnt >= 30:
        return 2
    else:
        if cnt >= 10:
            return 1     
    return 0      

# mxy's part
# 3.餐具卫士，金银铜
def cutleryGuardian(user_id:str):
    res = 0
    if bronze_cutleryGuardian(user_id) == True:
        res += 1
    if silver_cutleryGuardian(user_id) == True:
        res += 1
    if gold_cutleryGuardian(user_id) == True:
        res += 1
    return res

# 4.未来旅客，金银铜
def traveler(user_id:str):
    res = 0
    if bronze_traveler(user_id) == True:
        res += 1
    if silver_traveler(user_id) == True:
        res += 1
    if gold_traveler(user_id) == True:
        res += 1
    return res

# 9.步未来旅行家，金银铜
def master_traveler(user_id:str):
    res = 0
    if bronze_master_traveler(user_id) == True:
        res += 1
    if silver_master_traveler(user_id) == True:
        res += 1
    if gold_master_traveler(user_id) == True:
        res += 1
    return res

# 使用可回收餐具1次,后期注意换算的问题
def bronze_cutleryGuardian(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=3 and userid=%s",[user_id])
    results = cursor.fetchall()

    for each in results:
        if each[0] >= 1: # 建模后要更改
            return True
    return False

# 累计使用可回收餐具10天
def silver_cutleryGuardian(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=3 and userid=%s",[user_id])
    results = cursor.fetchall()
    cnt = 0
    for each in results:
        if each[0] >= 1:
            cnt += 1
    if cnt >= 10:
        return True
    return False

# 累计使用可回收餐具30天
def gold_cutleryGuardian(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=3 and userid=%s",[user_id])
    results = cursor.fetchall()
    cnt = 0
    for each in results:
        if each[0] >= 1:
            cnt += 1
    if cnt >= 30:
        return True
    return False

# 乘坐公共交通1次,后期注意换算的问题
def bronze_traveler(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=4 and userid=%s",[user_id])
    results = cursor.fetchall()

    for each in results:
        if each[0] >= 1: # 建模后要更改
            return True
    return False

# 累计乘坐公共交通10天
def silver_traveler(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=4 and userid=%s",[user_id])
    results = cursor.fetchall()
    cnt = 0
    for each in results:
        if each[0] >= 1:
            cnt += 1
    if cnt >= 10:
        return True
    return False

# 累计乘坐公共交通30天
def gold_traveler(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=4 and userid=%s",[user_id])
    results = cursor.fetchall()
    cnt = 0
    for each in results:
        if each[0] >= 1:
            cnt += 1
    if cnt >= 30:
        return True
    return False

# 累计乘坐公共交通50次
def bronze_master_traveler(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=4 and userid=%s",[user_id])
    results = cursor.fetchall()
    sum = 0
    for each in results:
        sum += each[0]
    if sum >= 50:
        return True
    return False

# 累计乘坐公共交通100次
def silver_master_traveler(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=4 and userid=%s",[user_id])
    results = cursor.fetchall()
    sum = 0
    for each in results:
        sum += each[0]
    if sum >= 100:
        return True
    return False

# 累计乘坐公共交通200次
def gold_master_traveler(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=4 and userid=%s",[user_id])
    results = cursor.fetchall()
    sum = 0
    for each in results:
        sum += each[0]
    if sum >= 200:
        return True
    return False

# zlh's part
##### 8.餐具收藏家 #####
def chop_collector(userID:str):
    res = 0
    if third_chop(userID) == True:
        res += 1
    if second_chop(userID) == True:
        res += 1
    if first_chop(userID) == True:
        res += 1
    return res #res为1：餐具收藏家（铜），2:银，3:金

# 累计上传50次
def third_chop(userID:str):
    cursor = connection.cursor()
    cursor.execute("select plogName from Plog where plogTypeID=3 and userID=%s",[userID])
    results = cursor.fetchall()
    res = False

    if len(results) >= 50:
        res = True
    return res

# 累计上传100次
def second_chop(userID:str):
    cursor = connection.cursor()
    cursor.execute("select plogName from Plog where plogTypeID=3 and userID=%s",[userID])
    results = cursor.fetchall()
    res = False

    if len(results) >= 100:
        res = True
    return res

# 累计上传200次
def first_chop(userID:str):
    cursor = connection.cursor()
    cursor.execute("select plogName from Plog where plogTypeID=3 and userID=%s",[userID])
    results = cursor.fetchall()
    res = False

    if len(results) >= 200:
        res = True
    return res

##### 5.爱心使者 #####
def clothes(userID:str):
    res = 0
    if bronze_clothes(userID) == True:
        res += 1
    return res #res为1：爱心使者（金）

# 衣物回收一次 
def bronze_clothes(userID:str):
    cursor = connection.cursor()
    cursor.execute("select plogName from Plog where plogTypeID=5 and userID=%s",[userID])
    results = cursor.fetchall()
    res = False

    if len(results) > 0:
        res = True
    return res

##### 10.爱心大使 #####
def clothes_lover(userID:str):
    res = 0
    if third_clothes(userID) == True:
        res += 1
    if second_clothes(userID) == True:
        res += 1
    if first_clothes(userID) == True:
        res += 1
    return res #res为1：爱心大使（铜），2:银，3:金

# 衣物回收累计10次
def third_clothes(userID:str):
    cursor = connection.cursor()
    cursor.execute("select plogName from Plog where plogTypeID=5 and userID=%s",[userID])
    results = cursor.fetchall()
    res = False

    if len(results) >= 10:
        res = True
    return res

# 衣物回收累计20次
def second_clothes(userID:str):
    cursor = connection.cursor()
    cursor.execute("select plogName from Plog where plogTypeID=5 and userID=%s",[userID])
    results = cursor.fetchall()
    res = False

    if len(results) >= 20:
        res = True
    return res

# 衣物回收累计50次
def first_clothes(userID:str):
    cursor = connection.cursor()
    cursor.execute("select plogName from Plog where plogTypeID=5 and userID=%s",[userID])
    results = cursor.fetchall()
    res = False

    if len(results) >= 50:
        res = True
    return res