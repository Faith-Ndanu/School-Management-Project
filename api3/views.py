from django.shortcuts import render
from rest_framework.views import APIView
from teacher.models import Teacher
from .serializers import TeacherSerializer
from rest_framework.response import Response


class StudentListView(APIView):
    def get(self , request):
        teacher=Teacher.objects.all()
        serializer = TeacherSerializer(teacher,many=True)
        return Response(serializer.data)