import json
import uuid
import os
from django.conf import settings
import datetime
from django.conf import settings
from django.http import JsonResponse
from django.forms import model_to_dict
from django.shortcuts import render,HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.views import APIView
from django.db import connection
# 以json的格式返回给页面
from rest_framework.response import Response
from rest_framework.decorators import api_view
from showSchool import models
# from showSchool.models import Feature,ProvinceA,ProvinceB,ProvinceOther,SchoolInfo,SchoolType,SchoolScore,SchoolImg
from showSchool.models import SchoolImg, SchoolInfo, SchoolType, SchoolScore, \
    Feature, ProvinceA, ProvinceOther, ProvinceB, Province, Hotsearchschool, Userinfo, Major \
    , SchoolDetail, SylBuild, MajorDetail, CountryLine, Image,article,article_comment
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.db.models import Q
from utils.jwt_authenticate import JWTQueryParamsAuthentication
from utils.jwt_create_token import create_token


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
import hashlib
class Register(APIView):
    # def get(self,request,id):
    def post(self,request):
        data=request.data['params']
        hash_object = hashlib.md5((data['password']).encode('utf-8'))
        hashed_password=hash_object.hexdigest()
        userRegister=Userinfo.objects.create(username=data['username'],userpassword=hashed_password,collect_school='',like_article='')
        if userRegister:
            return Response({'msg':'注册成功','code':200})
        else:
            return Response({'msg':'注册失败','code':500})
class LoginSer(serializers.ModelSerializer):
    class Meta:
        model=Userinfo
        fields='__all__'
class Login(GenericAPIView):
    serializer_class = LoginSer
    def post(self,request):
        obj=request.data['params']
        username=obj['username']
        password=obj['password']
        print(obj)
        hash_object=hashlib.md5(password.encode('utf-8'))
        hash_input_password=hash_object.hexdigest()
        user_obj=Userinfo.objects.filter(username=username,userpassword=hash_input_password).first()
        current_user=user_obj.username
        print(current_user,'当前用户名++++++++++++++++')

        if not user_obj:
            return Response({'code': 401, 'error': '用户名或密码错误'})
        payload = {
            'user_id': user_obj.pk,  # 自定义用户id
            'username': current_user,  # 自定义用户名
            'exp':datetime.datetime.utcnow()+datetime.timedelta(days=7)
        }
        jwt_token = create_token(payload=payload)
        print(jwt_token, '当前的 token')
        return Response({'code': 200, 'token': jwt_token,'current_user':current_user})



# 获取专业型硕士的门类
class pm_ser(serializers.ModelSerializer):
    class Meta:
        model=Major
        fields=['level1_name']
class pm_class(APIView):
    def post(self,request):
        data=request.data['params']['data']
        pm_class=Major.objects.filter(major_class=data).values('level1_name').distinct()
        serialer=pm_ser(instance=pm_class,many=True)
        return Response(serialer.data)
    def get(self,request):
        pm_class=Major.objects.filter(major_class='专业型硕士').values('level1_name').distinct()
        serialer=pm_ser(instance=pm_class,many=True)
        return Response(serialer.data)
# class am_ser(serializers.ModelSerializer):
#     class Meta:
#         model=Major
#         fields=['level1_name']
# class am_class(APIView):
#     def get(self,request):
#         pm_class=Major.objects.filter(major_class='学术型硕士').values('level1_name').distinct()
#         serialer=pm_ser(instance=pm_class,many=True)
#         return Response(serialer.data)

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
        major_list = Major.objects.distinct().all()
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
                    major_list = Major.objects.filter(major_class=obj['twoClass']).distinct()
                    serializer = detail_major(instance=major_list, many=True)
                    return Response(serializer.data)
                if 'level1_name' in obj:
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
        # print(data)
        school_list=SchoolDetail.objects.select_related('school_id').filter(school_id=data)
        serializer=singleSchoolInfo_ser(instance=school_list,many=True)
        return Response(serializer.data)

class allSchoolMajor(APIView):
    def post(self,request):
        data=request.data['params']['school_id']
        query="select * from school_score where school_name=(select school_name from school_info where school_id="+str(data)+")"
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        data = []
        for row in results:
            data.append({
                'learnType': row[0],
                'major_code': row[1],
                'major_name': row[2],
                'total': row[3],
                'politics': row[4],
                'english': row[5],
                'procourse': row[6],
                'procourese2': row[7],
                'remark': row[8],
            })
        return Response(data)

class chooseMajor(APIView):
    def post(self,request):
        school_id=request.data['params']['school_id']
        school_data=request.data['params']['data']
        if 'major' in  school_data and 'type' in school_data:
            learnType = school_data['type'].strip()
            query="select * from school_score where school_name=(select school_name from school_info where school_id="+str(school_id)+") and learnType='"+learnType+"' and major_name='"+school_data['major']+"'"
        elif 'major' in school_data:
            query="select * from school_score where school_name=(select school_name from school_info where school_id="+str(school_id)+") and major_name='"+school_data['major']+"'"
        else:
            learnType = school_data['type'].strip()
            query="select * from school_score where school_name=(select school_name from school_info where school_id="+str(school_id)+") and learnType='"+learnType+"'"
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        data = []
        for row in results:
            data.append({
                'learnType': row[0],
                'major_code': row[1],
                'major_name': row[2],
                'total': row[3],
                'politics': row[4],
                'english': row[5],
                'procourse': row[6],
                'procourese2': row[7],
                'remark': row[8],
            })
        return Response(data)

class syl_ser(serializers.ModelSerializer):
    class Meta:
        model=SylBuild
        fields='__all__'
class syl_jianshe(APIView):
    def post(self,request):
        data=request.data['params']['school_id']
        sql=SylBuild.objects.filter(school_id=data)
        serializer=syl_ser(instance=sql,many=True)
        return Response(serializer.data)

class shuoshizhuanyeSer(serializers.ModelSerializer):
    class Meta:
        model=MajorDetail
        fields='__all__'
class shuoshizhuanye(APIView):
    def post(self,request):
        data=request.data['params']['data']
        query="select * from shuoshizhuanye where school_id="+str(data)
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        data = []
        for row in results:
            data.append({
                'depart_id': row[0],
                'depart_name': row[1],
                'special_name': row[2],
                'special_code': row[3],
                'special_id': row[4],
                'school_id': row[5],
            })
        return Response(data)


class major_detail(APIView):
    def post(self,request):
        data=request.data['params']
        depart_id=data['depart_id']
        school_id=data['school_id']
        special_id=data['special_id']
        sql='select * from major_detail where school_id='+str(school_id)+' and depart_id='+str(depart_id)+' and special_id='+str(special_id)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()
        data=[]
        for row in results:
            data.append({
                'recruit_name':row[3],
                'special_name': row[4],
                'school_name': row[5],
                'depart_name': row[6],
                'year': row[7],
                'recruit_type': row[8],
                'level1': row[9],
                'level1_code': row[10],
                'level2': row[11],
                'level2_code': row[12],
                'recruit_number': row[13],
                'subject_name1': row[14],
                'subject1': row[15],
                'subject_name2': row[16],
                'subject2': row[17],
                'subject_name3': row[18],
                'subject3': row[19],
                'special_code':row[20]
            })
        return Response(json.dumps(data,ensure_ascii=False))

class regin(APIView):
    def get(self,request):
        sql='select name from province_a union select name from province_b union select name from province_other'
        with connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()
        return Response(json.dumps(results,ensure_ascii=False))



class userInfo(serializers.ModelSerializer):
    class Meta:
        model=Userinfo
        fields=['collect_school']
class collectSchool(APIView):

    def post(self,request):
        data=request.data['params']
        query="select collect_school from userinfo where username='"+data['user']+"'"
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            if str(data['school_id']) in results[0][0]:
                inx=results[0][0].find(str(data['school_id']))
                newres=results[0][0][:inx]+results[0][0][inx+1+len(str(data['school_id'])):].rstrip()

                sql = "update userinfo set collect_school='"+newres+"' where username='" + data['user'] + "'"

            else:
                sql="update userinfo set collect_school=concat('"+results[0][0]+"','"+str(data['school_id'])+",') where username='"+data['user']+"'"
            cursor.execute(sql)
            connection.commit()
            connection.close()
        return Response()


class getCollectSchool(APIView):
    def post(self,request):
        data=request.data['params']['username']
        query='select collect_school from userinfo where username="'+data+'"'
        with connection.cursor() as cursor:
            cursor.execute(query)
            res=cursor.fetchall()
            list=res[0][0].split(',')
            del(list[-1])
            school_data=[]
            for i in list:
                sql='select school_info.*,school_img.school_img from school_info left join school_img on school_info.school_name=school_img.school_name where school_id='+str(i)
                cursor.execute(sql)
                school_info=cursor.fetchall()
                for row in school_info:
                    school_data.append({
                        'school_id':row[12],
                        'school_type':row[1],
                        'type': row[2],
                        'area': row[3],
                        'school_name': row[5],
                        'province': row[10],
                        'school_img':row[13]
                    })
        return Response(json.dumps(school_data,ensure_ascii=False))

class isCollect(APIView):
    def post(self,request):
        data=request.data['params']
        res=models.Userinfo.objects.filter(username=data['user']).values('collect_school')
        datalist=list(res.values())
        if data['school_id'] in datalist[0]['collect_school']:
            return Response(True)
        else:
            return Response(False)

class userInfo_select_ser(serializers.ModelSerializer):
    class Meta:
        model=Userinfo
        fields='__all__'
class select_userInfo(APIView):
    def post(self,request):
        data=request.data['params']
        query=Userinfo.objects.filter(username=data['user']).all()
        serializer=userInfo_select_ser(instance=query,many=True)
        return Response(serializer.data)

class countryLine_ser(serializers.ModelSerializer):
    class Meta:
        model=CountryLine
        fields='__all__'
class contryLine(APIView):
    # def get(self,request):
    #     sql=CountryLine.objects.all()
    #     serializer=countryLine_ser(instance=sql,many=True)
    #     return Response(serializer.data)
    def post(self,request):
        data=request.data['params']
        year=data['year']
        sql=CountryLine.objects.filter(school_year=year)
        serializer=countryLine_ser(instance=sql,many=True)
        return Response(serializer.data)



import math
class schooltypePercent(APIView):
    def get(self,request):
        data = []
        sqlList=[
            'select count(*) from school_info where is_985=1;','select count(*) from school_info where is_211=1;','select count(*) from school_info where syl=1;',
            'select count(*) from school_info where type_school_name="科研院所";','select count(*) from school_info where type_school_name="高等院校";'
                 ]
        for i in sqlList:
            with connection.cursor() as cursor:
                cursor.execute(i)
                res = cursor.fetchall()
                # print(res)
                for i in res:
                    data.append(i[0])
        return Response(data)

class countryLineBigScreen(APIView):
    def get(self,request):
        year=[2021,2022,2023]
        major=['哲学','金融','电子信息','理学','历史学']
        sql=[]
        data=[]
        for k,v in enumerate(year):
            for a,b in enumerate(major):
                sql.append("select total from countryline where school_year="+str(v)+" and major_name='"+b+"' and area_type='A'")
        for i in sql:
            with connection.cursor() as cursor:
                cursor.execute(i)
                res = cursor.fetchall()
                # print(res)
                for i in res:
                    data.append(i[0])
        # print(data)
        return Response(data)


class everyProvinceNum(APIView):
    def get(self,request):
        regin=[]
        school_num=[]
        query='select name from province union select name from province_b union select name from province_other;'
        with connection.cursor() as cursor:
            cursor.execute(query)
            res = cursor.fetchall()
            for i in res:
                regin.append(i[0])
        for i in regin:
            sql="select count(*) from school_info where province_name='"+i+"'"
            with connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                if i in ['上海','北京','天津','重庆']:
                    school_num.append({
                        'name':(i+"市"),'value':result[0][0]
                    })
                elif i in ['内蒙古','西藏']:
                    school_num.append({
                        'name':(i+"自治区"),'value':result[0][0]
                    })
                elif i in ['新疆']:
                    school_num.append({
                        'name':'新疆维吾尔自治区','value':result[0][0]
                    })
                elif i in ['宁夏']:
                    school_num.append({
                        'name':(i+"回族自治区"),'value':result[0][0]
                    })
                elif i in ['广西']:
                    school_num.append({
                        'name':(i+"壮族自治区"),'value':result[0][0]
                    })
                elif i in ['香港','澳门']:
                    school_num.append({
                        'name': i, 'value': result[0][0]
                    })
                else:
                    school_num.append({
                        'name': i + "省", 'value': result[0][0]
                    })
        return Response(school_num)



class ImageSer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields='__all__'

from rest_framework.parsers import MultiPartParser, FormParser
# class userAvator(APIView):
#     def get(self,request):
#         return Response()
#     def post(self,request):
#         name = request.POST.get('name')
#         file = request.FILES.get('file')
#         print(name,file)
#         static_path = "media/photos"
#         # 将静态资源文件夹拼接到项目根目录
#         file_path = os.path.join(settings.BASE_DIR, static_path)
#         # 拼接图片名称
#         file_name = os.path.join(file_path, file.name)
#         if Image.objects.filter(name=name).exists():
#             currentUser=Image.objects.filter(name=name)
#             currentUser.update(image=file_name)
#         else:
#             query=Image.objects.create(name=name,image=file_name);
#             serializer=ImageSer(instance=query,many=True)
#         # 保存图片
#         # wb  以二进制形式写入
#         with open(file_name, "wb") as f:
#             # 写入字节流
#             f.write(file.file.read())
#         data = {
#             "code": 200,
#             'msg': "上传图片成功",
#             'static_path': static_path,
#         }
#         return Response(data)
#

from django.core.files.storage import FileSystemStorage
class upload_avator(APIView):
    authentication_classes = [JWTQueryParamsAuthentication, ]
    def post(self, request):
        name = request.POST.get('username')
        modifyName=request.data['modifyName']
        currentMajor=request.data['currentMajor']
        currentSchool=request.data['currentSchool']
        joinMajor=request.data['joinMajor']
        joinSchool=request.data['joinSchool']
        # print(len(request.data['year']).split(" "))
        year=request.data['year']
        # year=int(((request.data['year']).split(" "))[3])
        gender=request.data['gender']
        learnType=request.data['learnType']
        # print(int((year.split(" "))[3]))
        if request.FILES.get('file'):
            file = request.FILES.get('file')
            # print(name,file,currentMajor,currentSchool,joinMajor,joinSchool,year,gender,learnType,modifyName)
            fs = FileSystemStorage()
            if Userinfo.objects.filter(username=name).exists():

                filename = fs.save(file.name, file)
                uploaded_file_url = fs.url(filename)
                currentUser=Userinfo.objects.filter(username=name)
                currentUser.update(avator=uploaded_file_url,username=modifyName,gender=gender,grade=year,join_school=joinSchool,join_major=joinMajor,join_type=learnType,learn_major=currentMajor)
                return Response({'message':'修改成功','upload_url':uploaded_file_url,'username':modifyName},content_type="image/jpeg")
            else:
                filename = fs.save(file.name, file)
                uploaded_file_url = fs.url(filename)
                Userinfo.objects.create(username=name, avator=uploaded_file_url);
                return Response({'message':'添加成功','upload_url':uploaded_file_url},content_type="image/jpeg")
        else:
            if Userinfo.objects.filter(username=name).exists():
                currentUser=Userinfo.objects.filter(username=name)
                currentUser.update(username=modifyName,gender=gender,grade=year,join_school=joinSchool,join_major=joinMajor,join_type=learnType,learn_major=currentMajor)
                return Response({'message':'修改成功','username':modifyName},content_type="image/jpeg")
class upload_review(APIView):
    def post(self,request):
        file=request.FILES.get('file')
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        return Response({'url_upload_file':uploaded_file_url})
class getUserAvator(APIView):
    def post(self,request):
        data=request.data['params']['name']
        query=Image.objects.filter(name=data)
        serializer=ImageSer(instance=query,many=True)
        return Response(serializer.data)

# 学校级联选择器
class provinceSchool(APIView):
    def get(self,request):
        data=[]
        children=[]
        query = 'select name from province union select name from province_b union select name from province_other;'
        with connection.cursor() as cursor:
            cursor.execute(query)
            res = cursor.fetchall()
            for i in res:
                sql='select school_name from school_info where province_name="'+i[0]+'"'
                cursor.execute(sql)
                result=cursor.fetchall()
                children=[]
                for j in result:
                    children.append({
                        'value':j[0],
                        'label':j[0]
                    })
                data.append({
                    'value':i[0],
                    'label':i[0],
                    'children':children
                })
        return Response(data)
# 专业级联选择器
class majorChoose(APIView):
    def get(self,request):
        data=[]
        children=[]
        children2=[]
        list=('学术型硕士','专业型硕士')
        for i in list:
            query = 'select distinct level1_name from major where major_class="'+i+'"'
            with connection.cursor() as cursor:
                cursor.execute(query)
                res = cursor.fetchall()
                children=[]
                for j in res:
                    sql='select distinct major_name from major where level1_name="'+j[0]+'" and major_class="'+i+'"'
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    children2=[]
                    for k in result:
                        children2.append({
                            'label':k[0],
                            'value':k[0]
                        })
                    children.append({
                        'label':j[0],
                        'value':j[0],
                        'children':children2
                    })
                data.append({
                    'label': i,
                    'value': i,
                    'children':children
                })
        return Response(data)


class userInfoList(serializers.ModelSerializer):
    class Meta:
        model=Userinfo
        fields='__all__'
class getPrivate(APIView):
    authentication_classes = [JWTQueryParamsAuthentication, ]
    def post(self,request):
        data=request.data['params']['username']
        query='select username,gender,grade,join_school,join_major,join_type,learn_major,currentSchool,avator,like_article from userinfo where username="'+data+'"'
        with connection.cursor() as cursor:
            cursor.execute(query)
            res=cursor.fetchall()
        return Response(res)


class modify_secret(APIView):
    authentication_classes = [JWTQueryParamsAuthentication, ]
    def post(self,request):
        password=request.data['params']['password']
        hash_object = hashlib.md5(password.encode('utf-8'))
        hashed_input_password = hash_object.hexdigest()
        username=request.data['params']['username']
        query=Userinfo.objects.filter(username=username).update(userpassword=hashed_input_password)
        serializer=userInfo_select_ser(instance=query,many=False)
        return Response({'msg':'成功'})
class cancelAccount(APIView):
    authentication_classes = [JWTQueryParamsAuthentication,]
    def post(self,request):
        username=request.data['params']['username']
        password=request.data['params']['password']
        hash_object = hashlib.md5(password.encode('utf-8'))
        hashed_input_password = hash_object.hexdigest()
        user_obj=Userinfo.objects.filter(username=username,userpassword=hashed_input_password).first()
        if not user_obj:
            return Response({'error':'密码有误！'})
        else:
            Userinfo.objects.filter(username=username).delete()
            return Response({'msg':'注销成功','code':200})
class article_ser(serializers.ModelSerializer):
    class Meta:
        model=article
        fields='__all__'

from django.conf import settings
# 接收文章图片
class article_img(APIView):
    # authentication_classes = [JWTQueryParamsAuthentication, ]
    def post(self,request):
        name = request.POST.get('username')
        fs = FileSystemStorage(location=settings.MEDIA_ROOT + '/wangeditor/'+name+'/')
        uploaded_file = request.FILES.get('wangeditor-uploaded-image')
        file_path = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(file_path).split('/')[2]
        settings.MY_GLOBAL_VAR +=(url+',')
        return Response({'errno':0,'data':[{'url':'http://127.0.0.1:8000/media/wangeditor/'+name+'/'+url,'alt':'文章图片','href':'www.baidu.com'}]})

from django.utils import timezone
class acticle_content(APIView):
    authentication_classes = [JWTQueryParamsAuthentication, ]
    def post(self,request):
        now = timezone.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        data=request.data['params']
        username=data['username']
        article_content=data['article']
        article.objects.create(username=username,content=article_content,image=settings.MY_GLOBAL_VAR ,like=0,cur_time=str(formatted_time))
        settings.MY_GLOBAL_VAR=''
        return Response(data)
class article_list(APIView):
    def get(self,request):
        data = []
        query = 'select article.*,userinfo.avator from article left join userinfo on article.username=userinfo.username'
        with connection.cursor() as cursor:
            cursor.execute(query)
            res = cursor.fetchall()
            for i in res:
                img_list = ((i[0].decode('utf-8')).split(','))[:-1]
                data.append({
                    'username': i[5],
                    'content': i[1],
                    'id': i[2],
                    'like': i[3],
                    'cur_time':i[4],
                    'img_url': img_list,
                    'avator':i[6]
                })
        return Response(data)

class article_comment_ser(serializers.ModelSerializer):
    avator=userInfo_select_ser()
    class Meta:
        model=article_comment
        fields='__all__'
class user_comment(APIView):
    def post(self,request):
        data=request.data['params']
        article_comment.objects.create(article_id=data['article_id'],username=data['username'],comment=data['content'])
        return Response({'msg':'修改成功'})
class getAllComment(APIView):
    def get(self,request):
        data=[]
        query='select a.article_id,a.username,a.comment,b.avator from article_comment a left join userinfo b on a.username=b.username'
        with connection.cursor() as cursor:
            cursor.execute(query)
            res = cursor.fetchall()
            for i in res:
                data.append({
                'article_id':i[0],
                'username':i[1],
                'avator':i[3],
                'content':i[2]
                })

        return Response(data)

class dianzan(APIView):
    authentication_classes = [JWTQueryParamsAuthentication, ]
    def post(self,request):
        data=request.data['params']
        username=data['username']
        article_id=data['article_id']
        query='select like_article from userinfo where username="'+username+'"'
        with connection.cursor() as cursor:
            cursor.execute(query)
            res = cursor.fetchall()
            str_arr=''
            if str(article_id) in res[0][0]:
                arr=res[0][0].split(',')[:-1]
                str_index=arr.index(str(article_id))

                del arr[str_index]

                for i in arr:
                    str_arr+=(i+',')
                sql='update userinfo set like_article="'+str_arr+'" where username="'+username+'"'
                dianzan_article=article.objects.filter(number=article_id).values('like').first()
                if dianzan_article['like']>0:
                    article.objects.filter(number=article_id).update(like=(dianzan_article['like']-1))
                else:
                    article.objects.filter(number=article_id).update(like=0)

            else:
                # 不存在
                sql='update userinfo set like_article="'+res[0][0]+str(article_id)+'," where username="'+username+'"'
                dianzan_article=article.objects.filter(number=article_id).values('like').first()
                article.objects.filter(number=article_id).update(like=(dianzan_article['like']+1))
            cursor.execute(sql)
        return Response()

class school_score_ser(serializers.ModelSerializer):
    class Meta:
        model=SchoolScore
        fields='__all__'
class recommend(APIView):
    def post(self,request):
        recommend_school=[]
        data=request.data['params']
        score=int(data['score'])
        query='select distinct a.*,b.province_name,b.*,c.school_img from school_score a left join ' \
              'school_info b on a.school_name=b.school_name left join school_img c on a.school_name=c.school_name where province_name="'+data['region']+'" and learnType="'+data['class']+'" and major_name="'+data['major_class2']+'" and left(total,3)<='+str(score+20)+' order by left(total,3) asc '
        with connection.cursor() as cursor:
            cursor.execute(query)
            res = cursor.fetchall()
            for i in res:
                recommend_school.append(i)
        return Response(recommend_school)
