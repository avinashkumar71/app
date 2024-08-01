from django.shortcuts import render
from .models import CategoryModel
from .serializer import CategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class CategoryApiView(APIView):
    def get(self,request,pk=None):
        jwt = request.COOKIES
        print('jwt ----> ',jwt)
        category_items  = CategoryModel.objects.all()
        serializer = CategorySerializer(category_items,many=True)
        return Response(serializer.data)
