from django.shortcuts import render

from rest_framework.views import APIView
from classes.models import Class
from .serializers import ClassSerializer
from rest_framework.response import Response


class ClassListView(APIView):
    def get(self , request):
        classes=Class.objects.all()
        serializer = ClassSerializer(classes,many=True)
        return Response(serializer.data)



# Create your views here.
