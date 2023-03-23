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
from django.contrib import admin
from django.urls import path,include,re_path

from showSchool import views
from django.contrib import admin
from showSchool.views import allSchool,allSchoolType,province_a,province_b,province_other,allFeature,hotSchool,Register,Login,pm_class,am_class
from django.urls import path

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
    path('Resgiter/',Register.as_view()),
    path('Login/', Login.as_view()),
    path('pm_class/',pm_class.as_view()),
    path('am_class/',am_class.as_view())

]

