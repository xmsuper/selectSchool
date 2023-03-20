from django.forms import model_to_dict
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
# from showSchool.models import Feature,ProvinceA,ProvinceB,ProvinceOther,SchoolInfo,SchoolType,SchoolScore,SchoolImg
from showSchool.models import SchoolImg,SchoolInfo,SchoolType,SchoolScore,Feature,ProvinceA,ProvinceOther,ProvinceB,Province,hotSchoolSearch,userInfo

class allimgSer(serializers.ModelSerializer):
    class Meta:
        model=SchoolImg
        fields='__all__'
class allschoolInfoSer(serializers.ModelSerializer):

    school_name=allimgSer()
    class Meta:
        model=SchoolInfo
        fields='__all__'

class allSchool(ListCreateAPIView):
    # 指定查询集
    queryset = SchoolInfo.objects.all()
    # 指定序列化器
    serializer_class=allschoolInfoSer

class schoolTypeSer(serializers.ModelSerializer):
    class Meta:
        model=SchoolType
        fields='__all__'

class allSchoolType(ListCreateAPIView):
    queryset = SchoolType.objects.all()
    serializer_class = schoolTypeSer

class province_bSer(serializers.ModelSerializer):
    class Meta:
        model=ProvinceB
        fields='__all__'

class province_b(ListCreateAPIView):
    queryset = ProvinceB.objects.all()
    serializer_class = province_bSer
class province_otherSer(serializers.ModelSerializer):
    class Meta:
        model=ProvinceOther
        fields='__all__'

class province_other(ListCreateAPIView):
    queryset = ProvinceOther.objects.all()
    serializer_class = province_otherSer
class province_aSer(serializers.ModelSerializer):
    class Meta:
        model=ProvinceA
        fields='__all__'

class province_a(ListCreateAPIView):
    queryset = ProvinceA.objects.all()
    serializer_class = province_aSer

class featureSer(serializers.ModelSerializer):
    class Meta:
        model=Feature
        fields='__all__'

class allFeature(ListCreateAPIView):
    queryset = Feature.objects.all()
    serializer_class = featureSer

# 热搜院校
class hotSchool(serializers.ModelSerializer):
    school_name=allimgSer()
    class Meta:
        model=hotSchoolSearch
        fields='__all__'
class hotSchool(ListCreateAPIView):
    queryset = hotSchoolSearch.objects.all()
    serializer_class = hotSchool

class RegisterSer(serializers.ModelSerializer):
    class Meta:
        model=userInfo
        fields='__all__'
class Register(APIView):
    # def get(self,request,id):

    def post(self,request):
        # print(request.data)
        serializer=RegisterSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print('同名账户以存在')
            return Response(serializer.errors)
class LoginSer(serializers.ModelSerializer):
    class Meta:
        model=userInfo
        fields='__all__'
class Login(APIView):
    def post(self,request):
        # print((request.data))
        obj=request.data['params']
        print(obj)
        # username=obj['username']
        # password=obj['password']
        # serializer=RegisterSer(data=request.data)
        # if serializer.is_valid():
        return Response({'content':'成功'})