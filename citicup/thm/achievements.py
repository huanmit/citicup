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


def walker(user_id:str):
    res = 0
    if bronze_walker(user_id) == True:
        res += 1
    if silver_walker(user_id) == True:
        res += 1
    if gold_walker(user_id) == True:
        res += 1
    return res

def rider(user_id:str):
    res = 0
    return res

def chop(user_id:str):
    res = 0
    return res

def public(user_id:str):
    res = 0
    return res

def clothes(user_id:str):
    res = 0
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
    
    if len(results) >= 10:
        return True
    return False

# 累计上传步行30天
def gold_walker(user_id:str):
    cursor = connection.cursor()
    cursor.execute("select carbonCurrency from footprint where plogtypeid=1 and userid=%s",[user_id])
    results = cursor.fetchall()
    
    if len(results) >= 30:
        return True
    return False

