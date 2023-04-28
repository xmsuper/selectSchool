"""kaoyan_houduan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include,re_path

from kaoyan_houduan import settings
from showSchool import views
from django.contrib import admin
from showSchool.views import allSchool, allSchoolType, province_a, province_b, province_other \
    , allFeature, hotSchool, Login, pm_class, showTwoClass, \
    subject_class, detail_major_list, detail_school_list, searchResult, searchMajor, singSchoolInfo \
    , allSchoolMajor, chooseMajor, syl_jianshe, shuoshizhuanye, major_detail, regin, \
    collectSchool, getCollectSchool, isCollect, select_userInfo, contryLine \
    , schooltypePercent, countryLineBigScreen\
    , everyProvinceNum,getUserAvator,upload_avator,provinceSchool\
    ,majorChoose,getPrivate,upload_review,modify_secret,article_img,acticle_content,\
    article_list,user_comment,getAllComment,dianzan,recommend,Register,cancelAccount
from django.urls import path
from django.urls import include
from user.urls import path
# am_class

urlpatterns = [
    path('admin/',admin.site.urls),
    path('allSchool/',allSchool.as_view()),
    # path('test/',views.test),
    # path('allSchool2/', views.allSchool2)
    path('allSchoolType/',allSchoolType.as_view()),
    path('province_a/',province_a.as_view()),
    path('province_b/', province_b.as_view()),
    path('province_other/', province_other.as_view()),
    path('allFeature/', allFeature.as_view()),
    path('hotSchool/',hotSchool.as_view()),
    path('Register',Register.as_view()),
    path('Login', Login.as_view()),
    path('cancelAccount',cancelAccount.as_view()),
    path('pm_class/',pm_class.as_view()),
    path('pm_class',pm_class.as_view()),
    # path('am_class/',am_class.as_view()),
    path('showTwoClass/',showTwoClass.as_view()),
    path('subject_class',subject_class.as_view()),
    path('detail_major_list',detail_major_list.as_view()),
    path('detail_school_list',detail_school_list.as_view()),
    path('searchResult',searchResult.as_view()),
    path('searchMajor',searchMajor.as_view()),
    path('singSchoolInfo',singSchoolInfo.as_view()),
    # path('singSchoolInfo', singSchoolInfo.as_view({'get': 'list'})),
    path('allSchoolMajor',allSchoolMajor.as_view()),
    path('chooseMajor', chooseMajor.as_view()),
    path('syl_jianshe',syl_jianshe.as_view()),
    path('shuoshizhuanye',shuoshizhuanye.as_view()),
    path('major_detail',major_detail.as_view()),

    path('regin/',regin.as_view()),

    path('collectSchool',collectSchool.as_view()),
    path('getCollectSchool',getCollectSchool.as_view()),
    path('isCollect',isCollect.as_view()),
    path('select_userInfo',select_userInfo.as_view()),

    path('contryLine', contryLine.as_view()),
    path('schooltypePercent/',schooltypePercent.as_view()),
    path('countryLineBigScreen/', countryLineBigScreen.as_view()),
    path('everyProvinceNum/',everyProvinceNum.as_view()),

    path('user/',include('user.urls')),
    path('getUserAvator',getUserAvator.as_view()),
    path('upload_avator',upload_avator.as_view()),
    path('provinceSchool/',provinceSchool.as_view()),
    path('majorChoose/',majorChoose.as_view()),
    path('getPrivate',getPrivate.as_view()),
    path('upload_review',upload_review.as_view()),
    path('modify_secret',modify_secret.as_view()),
    path('article_img',article_img.as_view()),
    path('acticle_content',acticle_content.as_view()),
    path('article_list/',article_list.as_view()),
    path('user_comment',user_comment.as_view()),
    path('getAllComment/',getAllComment.as_view()),
    path('dianzan',dianzan.as_view()),
    path('recommend',recommend.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

