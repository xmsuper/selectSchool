# import http
#
# from django.db import models
# from django.template.context_processors import media
# #
# # class Image(models.Model):
# #     name = models.CharField(max_length=30)
# #     image = models.ImageField(upload_to='media.photos/')#该函数需要安装第三方包pillow
# #     class Meta:
# #         managed=True
# #         db_table='userAvator'
#
#
# class article2(models.Model):
#     content=models.TextField()
#     username=models.CharField(max_length=50)
#     number=models.AutoField(primary_key=True)
#     image=models.ImageField(upload_to='articlePhoto/')
#     like=models.IntegerField()
#     my_date = models.TextField()
#     class Meta:
#         managed=True
#         db_table='article'
# class article_comment2(models.Model):
#     username=models.CharField(max_length=50)
#     comment=models.TextField()
#     article_id=models.IntegerField()
#
#     class Meta:
#         managed=True
#         db_table='article_comment'
