from django.contrib import admin
from django.utils.html import format_html
from showSchool.models import SchoolImg,SchoolInfo,SchoolType,SchoolScore\
    ,SchoolDetail,Hotsearchschool,MajorDetail,Major,article,article_comment\
    ,CountryLine,SylBuild,Userinfo

class SchoolInfoAdmin(admin.ModelAdmin):
    #list_display表示：设置可显示的字段
    list_display =('school_name','type_name','province_area','type_school_name','province_name','rk_rank','is_985','is_211','is_zihuaxian')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # # ordering设置默认排序字段，负号表示降序排序
    ordering = ('school_id',)
    # # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # # 搜索功能及能实现搜索的字段
    search_fields = ('school_name__school_name','province_name')

class SchoolScoreAdmin(admin.ModelAdmin):
    list_display =('school_name','learntype','major_code','major_name','total','politics','english','procourse','procourese2','remark')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # # ordering设置默认排序字段，负号表示降序排序
    # ordering = ('',)
    # # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # # 搜索功能及能实现搜索的字段
    search_fields = ('school_name','major_name')

class SchoolDetailAdmin(admin.ModelAdmin):
    list_display =('school_name','belongsto','create_date','intro','num_lab','num_master','num_subject','school_space','school_address','province','school_phone','zhaoban_phone','school_site','zhaoban_site','school_email')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # # ordering设置默认排序字段，负号表示降序排序
    # ordering = ('',)
    # # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # # 搜索功能及能实现搜索的字段
    search_fields = ('school_name',)

class MajorAdmin(admin.ModelAdmin):
    list_display = ('major_name','major_code','major_class','level1_name','level2_name','spe_id')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-major_code',)
    # # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # # 搜索功能及能实现搜索的字段
    search_fields = ('major_name','major_code')

class SchoolImgAdmin(admin.ModelAdmin):
    list_display = ('school_name','school_img')
    list_per_page = 50
    search_fields = ('school_name',)
class MajorDetailAdmin(admin.ModelAdmin):
    list_display = ('special_code','depart_name','special_name','school_name','year','recruit_type','level1','level1_code','level2','level2_code','recruit_number','subject_name1','subject1','subject_name2','subject2','subject_name3','subject3')
    list_per_page = 50
    search_fields = ('school_name','special_code','depart_name','special_name')

class SylBuildAdmin(admin.ModelAdmin):
    list_display = ('school_id','syl_jianshe')
    ordering = ('-syl_jianshe',)

class CountryLineAdmin(admin.ModelAdmin):
    list_display = ('major_name','degree_type','area_type','code','school_year','total','single_100','single_150')
    ordering = ('-school_year',)
    search_fields = ('major_name','area_type','code')

class articleAdmin(admin.ModelAdmin):
    list_display = ('username','number','content','like','cur_time',)
    ordering = ('-cur_time',)
    search_fields = ('username','cur_time')
class article_commentAdmin(admin.ModelAdmin):
    list_display = ('username','comment','article_id')
    search_fields = ('username','article_id')
class HotsearchschoolAdmin(admin.ModelAdmin):
    list_display = ('school_name','school_id')

class UserinfoAdmin(admin.ModelAdmin):
    list_display = ('id','username','userpassword','gender','location','grade','join_school','join_major','join_type','learn_major','currentSchool','like_article')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)

    # # 搜索功能及能实现搜索的字段
    search_fields = ('username',)

admin.site.register(SchoolInfo,SchoolInfoAdmin)
admin.site.register(SchoolImg,SchoolImgAdmin)
admin.site.register(SchoolDetail,SchoolDetailAdmin)
admin.site.register(SchoolScore,SchoolScoreAdmin)
admin.site.register(article,articleAdmin)
admin.site.register(article_comment,article_commentAdmin)
admin.site.register(CountryLine,CountryLineAdmin)
admin.site.register(Hotsearchschool,HotsearchschoolAdmin)
admin.site.register(SylBuild,SylBuildAdmin)
admin.site.register(Major,MajorAdmin)
admin.site.register(MajorDetail,MajorDetailAdmin)
admin.site.register(Userinfo,UserinfoAdmin)
admin.site.site_header = '考研后台'