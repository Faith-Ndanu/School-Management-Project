from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from rest_framework.response import Response


class ClassPeriodListView(APIView):
    def get(self , request):
        classperiod=ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod,many=True)
        return Response(serializer.data)