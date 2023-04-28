from django.shortcuts import render
from rest_framework import serializers

from user import models
# from user.models import Image
from rest_framework.views import APIView
from django.db import connection
# 以json的格式返回给页面
from rest_framework.response import Response
# from user.models import Image
# Create your views here.

MEDIA_SERVER = 'http://127.0.0.1:8000/media/'
def image(request):
    if request.method == 'GET':
        return render(request, 'image.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        images = Image(name=name, image=image)
        images.save()
        return render(request, 'image_show.html', {'images': images})
#
# class ImageSer(serializers.ModelSerializer):
#     class Meta:
#         model=Image
#         field='__all__'
# class userAvator(APIView):
#     def get(self,request):
#         return Response()
#     def post(self,request):
#         serializer=ImageSer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data)
#         return Response(serializer.errors)