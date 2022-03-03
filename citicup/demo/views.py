from urllib import request
from django.shortcuts import render
from django import http
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView


class BookAPIView(APIView):
    def get(self,request):
        # get apiview get params
        print(request.query_params)
        return http.HttpResponse("get")

    def post(self,request):
        print(request.data)
        return http.HttpResponse("post")