# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Feature(models.Model):
    name = models.CharField(unique=True, max_length=10, blank=True, null=True)
    code = models.CharField(unique=True, max_length=20, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    feature_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'feature'


class Hotsearchschool(models.Model):
    school_id = models.CharField(primary_key=True, max_length=20)
    school_name = models.ForeignKey('SchoolImg', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hotsearchschool'


class Major(models.Model):
    major_name = models.CharField(max_length=50)
    major_code = models.CharField(max_length=50)
    major_class = models.CharField(max_length=10)
    level1_name = models.CharField(max_length=50)
    level2_name = models.CharField(max_length=50)
    spe_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'major'


class Province(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province'


class ProvinceA(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province_a'


class ProvinceB(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province_b'


class ProvinceOther(models.Model):
    code = models.IntegerField(primary_key=True)
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
    # schoolDetail=models.OneToOneField(SchoolDetail,on_delete=models.CASCADE,related_name='schoolDetail')

    class Meta:
        managed = True
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


class Userinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    collect_school = models.TextField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=50)
    userpassword = models.CharField(db_column='userPassword', max_length=80)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userinfo'
class SchoolDetail(models.Model):
    belongsto = models.CharField(db_column='belongsTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(max_length=50, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    num_doctor = models.IntegerField(blank=True, null=True)
    num_lab = models.IntegerField(blank=True, null=True)
    num_master = models.IntegerField(blank=True, null=True)
    num_subject = models.IntegerField(blank=True, null=True)
    school_space = models.CharField(max_length=50, blank=True, null=True)
    school_name = models.TextField(blank=True, null=True)
    school_address = models.TextField(blank=True, null=True)
    province = models.TextField(blank=True, null=True)
    school_img = models.TextField(blank=True, null=True)
    school_phone = models.CharField(max_length=50, blank=True, null=True)
    zhaoban_phone = models.CharField(max_length=50, blank=True, null=True)
    school_site = models.TextField(blank=True, null=True)
    zhaoban_site = models.TextField(blank=True, null=True)
    school_email = models.TextField(blank=True, null=True)
    school_id = models.OneToOneField(SchoolInfo,on_delete=models.CASCADE,primary_key=True,db_column='school_id')
    # model_b = models.OneToOneField('SchoolInfo', on_delete=models.CASCADE, related_name='model_a')

    class Meta:
        managed = True
        db_table = 'school_detail'

class SylBuild(models.Model):
    school_id=models.IntegerField(primary_key=True)
    syl_jianshe=models.TextField()
    class Meta:
        managed=True
        db_table='syl_build'
class MajorDetail(models.Model):
    school_id = models.IntegerField(blank=True, null=True)
    depart_id = models.IntegerField(blank=True, null=True)
    special_id = models.IntegerField(blank=True, null=True)
    recruit_name = models.CharField(max_length=50, blank=True, null=True)
    special_name = models.CharField(max_length=100, blank=True, null=True)
    school_name = models.TextField(blank=True, null=True)
    depart_name = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    recruit_type = models.CharField(max_length=50, blank=True, null=True)
    level1 = models.CharField(max_length=50, blank=True, null=True)
    level1_code = models.CharField(max_length=50, blank=True, null=True)
    level2 = models.CharField(max_length=100, blank=True, null=True)
    level2_code = models.CharField(max_length=50, blank=True, null=True)
    recruit_number = models.IntegerField(blank=True, null=True)
    subject_name1 = models.TextField(blank=True, null=True)
    subject1 = models.TextField(blank=True, null=True)
    subject_name2 = models.TextField(blank=True, null=True)
    subject2 = models.TextField(blank=True, null=True)
    subject_name3 = models.TextField(blank=True, null=True)
    subject3 = models.TextField(blank=True, null=True)
    special_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'major_detail'