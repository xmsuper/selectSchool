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

    class Meta:
        managed = False
        db_table = 'feature'


class ProvinceA(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province_a'


class ProvinceB(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province_b'


class ProvinceOther(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province_other'


class SchoolInfo(models.Model):
    is_211 = models.IntegerField()
    type_name = models.CharField(max_length=50, blank=True, null=True)
    type_school_name = models.CharField(max_length=50)
    province_area = models.CharField(max_length=10)
    syl = models.IntegerField(blank=True, null=True)
    school_name = models.CharField(max_length=50)
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

    class Meta:
        managed = False
        db_table = 'school_type'
