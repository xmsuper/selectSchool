import json
from django.http import JsonResponse
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
from rest_framework import viewsets
from rest_framework.views import APIView
from django.db import connection
# 以json的格式返回给页面
from rest_framework.response import Response
# from showSchool.models import Feature,ProvinceA,ProvinceB,ProvinceOther,SchoolInfo,SchoolType,SchoolScore,SchoolImg
from showSchool.models import SchoolImg,SchoolInfo,SchoolType,SchoolScore,\
    Feature,ProvinceA,ProvinceOther,ProvinceB,Province,Hotsearchschool,Userinfo,Major\
    ,SchoolDetail
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.db.models import Q
class allimgSer(serializers.ModelSerializer):
    class Meta:
        model=SchoolImg
        fields='__all__'
class allschoolInfoSer(serializers.ModelSerializer):

    school_name=allimgSer()
    class Meta:
        model=SchoolInfo
        fields='__all__'
class searchSchoolser(serializers.ModelSerializer):
    class Meta:
        model=SchoolInfo
        fields='__all__'

# 搜索院校信息
class searchResult(APIView):
    def post(self,request):
        obj=request.data['params']['keyword']
        print(obj)
        # 外键模糊查询，需要后面在跟一个school_name__school_name__icontains=''
        sql=SchoolInfo.objects.filter(school_name__school_name__icontains=obj['keyword'])
        serializer=allschoolInfoSer(instance=sql,many=True)
        return Response(serializer.data)
# 搜索专业信息
class majorList(serializers.ModelSerializer):
    class Meta:
        model=Major
        fields='__all__'
class searchMajor(APIView):
    def post(self,request):
        obj=request.data['params']['keyword']
        sql=Major.objects.filter(major_name__icontains=obj['keyword'])
        serializer=majorList(instance=sql,many=True)
        return Response(serializer.data)

# 查询所有院校信息
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
        model=Hotsearchschool
        fields='__all__'
class hotSchool(ListCreateAPIView):
    queryset = Hotsearchschool.objects.all()
    serializer_class = hotSchool

class RegisterSer(serializers.ModelSerializer):
    class Meta:
        model=Userinfo
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
        model=Userinfo
        fields='__all__'
class Login(GenericAPIView):
    serializer_class = LoginSer
    def post(self,request):
        # print((request.data))
        obj=request.data['params']
        username=obj['username']
        password=obj['password']
        result=Userinfo.objects.filter(username=username,userPassword=password)
        if len(result)>0:
            return Response({'content':'成功','code':200})
        else:
            return Response({'content':'登录失败','code':'400'})


# 获取专业型硕士的门类
class pm_ser(serializers.ModelSerializer):
    class Meta:
        model=Major
        fields=['level1_name']
class pm_class(APIView):
    def get(self,request):
        pm_class=Major.objects.filter(major_class='专业型硕士').values('level1_name').distinct()
        serialer=pm_ser(instance=pm_class,many=True)
        return Response(serialer.data)
class am_ser(serializers.ModelSerializer):
    class Meta:
        model=Major
        fields=['level1_name']
class am_class(APIView):
    def get(self,request):
        pm_class=Major.objects.filter(major_class='学术型硕士').values('level1_name').distinct()
        serialer=pm_ser(instance=pm_class,many=True)
        return Response(serialer.data)

class two_class_ser(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['major_class']

class showTwoClass(APIView):
    def get(self, request):
        two_class=Major.objects.values('major_class').distinct()
        serializer=two_class_ser(instance=two_class,many=True)
        return Response(serializer.data)

class majorList_ser(serializers.ModelSerializer):
    class Meta:
        model=Major
        fields=['level2_name']
class subject_class(APIView):
    def post(self,request):
        obj=request.data['params']
        match len(obj):
            case 2:
                major_list=Major.objects.filter(major_class=obj['twoClass']).filter(level1_name=obj['level1_name']).values('level2_name').distinct()
                serializer=majorList_ser(instance=major_list,many=True)
                return Response(serializer.data)
        return Response()

# 查专业
class detail_major(serializers.ModelSerializer):
    class Meta:
        model=Major
        fields='__all__'
class detail_major_list(APIView):
    def get(self,request):
        major_list = Major.objects.all()
        serializer = detail_major(instance=major_list, many=True)
        return Response(serializer.data)
    def post(self,request):
        obj=request.data['params']
        match len(obj):
            case 3:
                major_list=Major.objects.filter(major_class=obj['twoClass']).filter(level1_name=obj['level1_name']).filter(level2_name=obj['level2_name'])
                serializer=detail_major(instance=major_list,many=True)
                return Response(serializer.data)
            case 2:
                major_list=Major.objects.filter(major_class=obj['twoClass']).filter(level1_name=obj['level1_name'])
                serializer=detail_major(instance=major_list,many=True)
                return Response(serializer.data)
            case 1:
                if 'twoClass' in obj:
                    print(obj['twoClass'])
                    major_list = Major.objects.filter(major_class=obj['twoClass']).distinct()
                    serializer = detail_major(instance=major_list, many=True)
                    return Response(serializer.data)
                if 'level1_name' in obj:
                    print(obj['level1_name'])
                    major_list = Major.objects.filter(level1_name=obj['level1_name'])
                    serializer = detail_major(instance=major_list, many=True)
                    return Response(serializer.data)
        return Response({'code':'200'})

# 查院校
class detail_school_ser(serializers.ModelSerializer):
    school_name = allimgSer()
    class Meta:
        model=SchoolInfo
        fields='__all__'
class detail_school_list(APIView):
    def post(self,request):
        obj=request.data['params']
        school_data=obj['data']
        print(school_data)
        match len(school_data):
            case 3:
                if school_data['SchoolTs']=='高等院校'or'科研院所':
                    detail_school_sql=SchoolInfo.objects.filter(province_name=school_data['Location']).filter(type_name=school_data['SchoolType']).filter(type_school_name=school_data['SchoolTs'])
                elif school_data['SchoolTs']=='985':
                    detail_school_sql = SchoolInfo.objects.filter(province_name=school_data['Location']).filter(
                        type_name=school_data['SchoolType']).filter(is_985=1)
                elif school_data['SchoolTs']=='211':
                    detail_school_sql = SchoolInfo.objects.filter(province_name=school_data['Location']).filter(
                        type_name=school_data['SchoolType']).filter(is_211=1)
                elif school_data['SchoolTs']=='双一流':
                    detail_school_sql = SchoolInfo.objects.filter(province_name=school_data['Location']).filter(
                        type_name=school_data['SchoolType']).filter(syl=1)
                else:
                    detail_school_sql = SchoolInfo.objects.filter(province_name=school_data['Location']).filter(
                        type_name=school_data['SchoolType']).filter(is_zihuaxian=1)
                serializer=detail_school_ser(instance=detail_school_sql,many=True)
                return Response(serializer.data)
            case 2:
                if 'SchoolTs'in school_data and 'Location' in school_data:
                    print('类型和地址')
                    match school_data['SchoolTs']:
                        case '高等院校'|'科研院所':
                            detail_school_sql = SchoolInfo.objects.filter(province_name=school_data['Location']).filter(type_school_name=school_data['SchoolTs'])
                        case '985':
                            detail_school_sql = SchoolInfo.objects.filter(province_name=school_data['Location']).filter(is_985=1)
                        case '211':
                            detail_school_sql = SchoolInfo.objects.filter(province_name=school_data['Location']).filter(is_211=1)
                        case '双一流':
                            detail_school_sql = SchoolInfo.objects.filter(province_name=school_data['Location']).filter(syl=1)
                        case '自划线':
                            detail_school_sql = SchoolInfo.objects.filter(province_name=school_data['Location']).filter(is_zihuaxian=1)
                    serializer = detail_school_ser(instance=detail_school_sql, many=True)
                    return Response(serializer.data)
                if 'SchoolTs'in school_data and 'SchoolType' in school_data:
                    match school_data['SchoolTs']:
                        case '高等院校' | '科研院所':
                            detail_school_sql = SchoolInfo.objects.filter(type_school_name=school_data['SchoolTs']).filter(type_name=school_data['SchoolType'])
                        case '985':
                            detail_school_sql = SchoolInfo.objects.filter(is_985=1).filter(
                                type_name=school_data['SchoolType'])
                        case '211':
                            detail_school_sql = SchoolInfo.objects.filter(is_211=1).filter(
                                type_name=school_data['SchoolType'])
                        case '双一流':
                            detail_school_sql = SchoolInfo.objects.filter(syl=1).filter(
                                type_name=school_data['SchoolType'])
                        case '自划线':
                            detail_school_sql = SchoolInfo.objects.filter(is_zihuaxian=1).filter(type_name=school_data['schoolType'])
                    serializer = detail_school_ser(instance=detail_school_sql, many=True)
                    return Response(serializer.data)
                if 'SchoolType' in school_data and 'Location' in school_data :
                    detail_school_sql = SchoolInfo.objects.filter(province_name=school_data['Location']).filter(type_name=school_data['SchoolType'])
                    serializer = detail_school_ser(instance=detail_school_sql, many=True)
                    return Response(serializer.data)
            case 1:
                if 'Location' in school_data:
                    detail_school_sql = SchoolInfo.objects.filter(province_name=school_data['Location'])
                    serializer = detail_school_ser(instance=detail_school_sql, many=True)
                    return Response(serializer.data)
                if 'SchoolType' in school_data:
                    detail_school_sql = SchoolInfo.objects.filter(type_name=school_data['SchoolType'])
                    serializer = detail_school_ser(instance=detail_school_sql, many=True)
                    return Response(serializer.data)
                if 'SchoolTs' in school_data:
                        match school_data['SchoolTs']:
                            case '高等院校'|'科研院所':
                                detail_school_sql = SchoolInfo.objects.filter(type_school_name=school_data['SchoolTs'])
                            case '985':
                                detail_school_sql = SchoolInfo.objects.filter(is_985=1)
                            case '211':
                                detail_school_sql = SchoolInfo.objects.filter(is_211=1)
                            case '双一流':
                                print('syl')
                                detail_school_sql = SchoolInfo.objects.filter(syl=1)
                            case '自划线':
                                detail_school_sql = SchoolInfo.objects.filter(is_zihuaxian=1)
                        serializer = detail_school_ser(instance=detail_school_sql, many=True)
                        return Response(serializer.data)
        return Response({'error':'错误'})

# class allschoolser(serializers.ModelSerializer):
#     school_name=allimgSer()
#     class Meta:
#         model=SchoolInfo
#         fields=('school_id','type_name','is_985','is_211','type_school_name','syl','province_area','school_img')

class singleSchoolInfo_ser(serializers.ModelSerializer):
    school_id=allschoolInfoSer()
    class Meta:
        model=SchoolDetail
        fields='__all__'

class singSchoolInfo(APIView):
    def post(self,request):
        data=request.data['params']['school_id']
        print(data)
        school_list=SchoolDetail.objects.select_related('school_id').filter(school_id=data)
        serializer=singleSchoolInfo_ser(instance=school_list,many=True)
        return Response(serializer.data)
        # sql=SchoolDetail.objects.filter(school_id=data)
        # serializer=singleSchoolInfo_ser(instance=sql,many=True)

        # query=' select a.school_id,a.school_name,b.school_email,a.is_985,a.is_211,a.is_zihuaxian' \
        #       ',a.province_area,a.province_name,b.belongsTo,b.create_date,b.intro,b.num_doctor,' \
        #       'b.num_lab,b.num_master,b.num_subject,b.school_space,b.school_site,b.zhaoban_site,' \
        #       'b.school_phone,b.zhaoban_phone from school_info a left join school_detail b ' \
        #       'on a.school_id =b.school_id where a.school_id='+str(data)
        # with connection.cursor() as cursor:
        #     cursor.execute(query)
        #     result=cursor.fetchall()
        #
        # return JsonResponse(json.dumps(result))

class detail_school_score_ser(serializers.ModelSerializer):
    class Meta:
        model=SchoolScore
        feilds='__all__'