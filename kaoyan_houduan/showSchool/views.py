from django.shortcuts import render,HttpResponse
# Feature
# ProvinceA
# ProvinceB
# ProvinceOther
# SchoolInfo
# SchoolScore
# SchoolType
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import ListCreateAPIView

from rest_framework import serializers
from rest_framework.views import APIView
# 以json的格式返回给页面
from rest_framework.response import Response
from showSchool.models import Feature,ProvinceA,ProvinceB,ProvinceOther,SchoolInfo,SchoolType,SchoolScore

# 构建序列化器
class allSchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model=SchoolInfo
        fields='__all__'
# class allSchool(GenericAPIView,ListModelMixin,CreateModelMixin):
#     # 指定查询集
#     queryset =SchoolInfo.objects
#     # 指定序列化器
#     serializer_class=allSchoolSerializers
#     def get(self,request):
#         return self.list(request)

class allSchool(ListCreateAPIView):
    # 指定查询集
    queryset =SchoolInfo.objects
    # 指定序列化器
    serializer_class=allSchoolSerializers