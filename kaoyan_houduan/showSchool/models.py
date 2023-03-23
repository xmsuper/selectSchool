# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser

"""
django内置的user对象，已经包含了一些主要的属性，如username,password,email等，实际使用可能还需要昵称等其他属性
通过AbstractUser可以进行扩展使用，添加用户自定义的属性
model中
from django.contrib.auth.models import AbstractUser
class MyUser(AbstractUser):
    pass
    
全局settings.py中配置，默认覆盖的user model
AUTH_USER_MODEL = 'app.MyUser'

"""
# class MyUser(AbstractUser):
#     phone=models.CharField(verbose_name='s手机号',max_length=11,null=True,unique=True)

class ApptestAuthor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'apptest_author'


class ApptestBook(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(ApptestAuthor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apptest_book'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'



class Feature(models.Model):
    name = models.CharField(unique=True, max_length=10, blank=True, null=True)
    code = models.CharField(primary_key=True,unique=True, max_length=20, blank=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    feature_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'feature'


class Province(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province'


class ProvinceA(models.Model):
    code = models.TextField(primary_key=True,blank=True)
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province_a'


class ProvinceB(models.Model):
    code = models.CharField(primary_key=True,max_length=10, blank=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province_b'


class ProvinceOther(models.Model):
    code = models.CharField(primary_key=True,max_length=10, blank=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province_other'


class SchoolImg(models.Model):
    school_name = models.CharField(primary_key=True, max_length=50)
    school_img = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_img'


class SchoolInfo(models.Model):
    is_211 = models.IntegerField()
    type_name = models.CharField(max_length=50, blank=True, null=True)
    type_school_name = models.CharField(max_length=50)
    province_area = models.CharField(max_length=10)
    syl = models.IntegerField(blank=True, null=True)
    school_name = models.ForeignKey(SchoolImg, models.DO_NOTHING, db_column='school_name')
    clicks = models.IntegerField(blank=True, null=True)
    is_985 = models.IntegerField(blank=True, null=True)
    is_zihuaxian = models.IntegerField(blank=True, null=True)
    rk_rank = models.IntegerField(blank=True, null=True)
    province_name = models.CharField(max_length=20, blank=True, null=True)
    is_ads = models.IntegerField(blank=True, null=True)
    school_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'school_info'


class SchoolScore(models.Model):
    learntype = models.CharField(db_column='learnType', max_length=10)  # Field name made lowercase.
    major_code = models.CharField(max_length=20)
    major_name = models.TextField()
    total = models.CharField(max_length=10, blank=True, null=True)
    politics = models.TextField(blank=True, null=True)
    english = models.TextField(blank=True, null=True)
    procourse = models.TextField(blank=True, null=True)
    procourese2 = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    school_name = models.TextField(blank=True, null=True)
    school_tel = models.TextField(blank=True, null=True)
    school_email = models.TextField(blank=True, null=True)
    school_web = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_score'


class SchoolType(models.Model):
    name = models.CharField(unique=True, max_length=10)
    code = models.CharField(unique=True, max_length=10)
    type = models.CharField(max_length=20, blank=True, null=True)
    type_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'school_type'

class hotSchoolSearch(models.Model):
    school_id=models.CharField(primary_key=True,null=False,max_length=20)
    school_name=models.ForeignKey(SchoolImg, max_length=50,on_delete=models.CASCADE)
    class Meta:
        managed=True
        db_table='hotSearchSchool'
class userInfo(models.Model):
    username=models.CharField(max_length=50,unique=True)
    userPassword=models.CharField(max_length=80)
    class Meta:
        managed=True
        db_table='userInfo'


class school_detail(models.Model):
    school_id = models.IntegerField(primary_key=True,null=False)
    belongsTo=models.CharField(max_length=50)
    create_date=models.IntegerField()
    intro=models.TextField()
    num_doctor=models.IntegerField()
    num_lab=models.IntegerField()
    num_master=models.IntegerField()
    num_subject=models.IntegerField()
    school_space=models.CharField(max_length=50)
    class Meta:
        managed=True
        db_table='school_detail'

class major(models.Model):
    major_name=models.CharField(max_length=50)
    major_code=models.CharField(max_length=50)
    major_class=models.CharField(max_length=10)
    level1_name=models.CharField(max_length=50)
    level2_name=models.CharField(max_length=50)
    spe_id=models.IntegerField(primary_key=True)
    class Meta:
        managed=True
        db_table='major'