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
from rest_framework.pagination import PageNumberPagination
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
class school_img(serializers.ModelSerializer):
    class Meta:
        # model=school_img
        fields='__all__'

class SchoolPageination(PageNumberPagination):
    # 每页展示条数
    page_size = 10
    # 查询页码参数  ？page=10
    # page_query_param = 'p'
    # 每页条数参数
    page_size_query_param = 'size'
    # 表示每页最大显示数量，做限制使用，避免突然大量的查询数据
    max_page_size = 20
class allSchool(ListCreateAPIView):
    # 指定查询集
    queryset =SchoolInfo.objects.all()
    # 指定序列化器
    serializer_class=allSchoolSerializers
    # 设置分页s
    # pagination_class = SchoolPageination
    # 'select a.school_name,b.school_img from school_info a left join school_img b on a.school_name=b.school_name'