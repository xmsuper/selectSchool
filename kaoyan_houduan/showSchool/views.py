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
from showSchool.models import SchoolImg,SchoolInfo,SchoolType,SchoolScore,Feature,ProvinceA,ProvinceOther,ProvinceB,Province,hotSchoolSearch,userInfo,major
from django.contrib.auth import get_user_model
from rest_framework import serializers
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
class Login(GenericAPIView):
    serializer_class = LoginSer
    def post(self,request):
        # print((request.data))
        obj=request.data['params']
        username=obj['username']
        password=obj['password']
        result=userInfo.objects.filter(username=username,userPassword=password)
        if len(result)>0:
            return Response({'content':'成功','code':200})
        else:
            return Response({'content':'登录失败','code':'400'})


# 获取专业型硕士的门类
class pm_ser(serializers.ModelSerializer):
    class Meta:
        model=major
        fields=['level1_name']
class pm_class(APIView):
    def get(self,request):
        pm_class=major.objects.filter(major_class='专业型硕士').values('level1_name').distinct()
        serialer=pm_ser(instance=pm_class,many=True)
        return Response(serialer.data)
class am_ser(serializers.ModelSerializer):
    class Meta:
        model=major
        fields=['level1_name']
class am_class(APIView):
    def get(self,request):
        pm_class=major.objects.filter(major_class='学术型硕士').values('level1_name').distinct()
        serialer=pm_ser(instance=pm_class,many=True)
        return Response(serialer.data)

class two_class_ser(serializers.ModelSerializer):
    class Meta:
        model = major
        fields = ['major_class']

class showTwoClass(APIView):
    def get(self, request):
        two_class=major.objects.values('major_class').distinct()
        serializer=two_class_ser(instance=two_class,many=True)
        return Response(serializer.data)

class majorList_ser(serializers.ModelSerializer):
    class Meta:
        model=major
        fields=['level2_name']
class subject_class(APIView):
    def post(self,request):
        obj=request.data['params']
        match len(obj):
            case 2:
                major_list=major.objects.filter(major_class=obj['twoClass']).filter(level1_name=obj['level1_name']).values('level2_name').distinct()
                serializer=majorList_ser(instance=major_list,many=True)
                return Response(serializer.data)
        return Response()

# 查专业
class detail_major(serializers.ModelSerializer):
    class Meta:
        model=major
        fields='__all__'
class detail_major_list(APIView):
    def get(self,request):
        major_list = major.objects.all()
        serializer = detail_major(instance=major_list, many=True)
        return Response(serializer.data)
    def post(self,request):
        obj=request.data['params']
        print(type(obj))
        match len(obj):
            case 3:
                major_list=major.objects.filter(major_class=obj['twoClass']).filter(level1_name=obj['level1_name']).filter(level2_name=obj['level2_name'])
                serializer=detail_major(instance=major_list,many=True)
                return Response(serializer.data)
            case 2:
                major_list=major.objects.filter(major_class=obj['twoClass']).filter(level1_name=obj['level1_name'])
                serializer=detail_major(instance=major_list,many=True)
                return Response(serializer.data)
            case 1:
                if 'twoClass' in obj:
                    print(obj['twoClass'])
                    major_list = major.objects.filter(major_class=obj['twoClass']).distinct()
                    serializer = detail_major(instance=major_list, many=True)
                    return Response(serializer.data)
                if 'level1_name' in obj:
                    print(obj['level1_name'])
                    major_list = major.objects.filter(level1_name=obj['level1_name'])
                    serializer = detail_major(instance=major_list, many=True)
                    return Response(serializer.data)

        return Response({'code':'200'})


