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

# 餐具卫士，金银铜
def cutleryGuardian(user_id:str):
    res = 0
    if bronze_cutleryGuardian(user_id) == True:
        res += 1
    if silver_cutleryGuardian(user_id) == True:
        res += 1
    if gold_cutleryGuardian(user_id) == True:
        res += 1
    return res

# 未来旅客，金银铜
def traveler(user_id:str):
    res = 0
    if bronze_traveler(user_id) == True:
        res += 1
    if silver_traveler(user_id) == True:
        res += 1
    if gold_traveler(user_id) == True:
        res += 1
    return res

# 步未来旅行家，金银铜
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