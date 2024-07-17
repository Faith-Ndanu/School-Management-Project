from django.shortcuts import render

from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from course.models import Course
from .serializers import CourseSerializer
from classes.models import Class
from .serializers import ClassSerializer
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from rest_framework.response import Response


class StudentListView(APIView):
    def get(self , request):
        teacher=Teacher.objects.all()
        serializer = TeacherSerializer(teacher,many=True)
        return Response(serializer.data)



class ClassPeriodListView(APIView):
    def get(self , request):
        classperiod=ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod,many=True)
        return Response(serializer.data)


class StudentListView(APIView):
    def get(self , request):
        students=Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)


class ClassListView(APIView):
    def get(self , request):
        classes=Class.objects.all()
        serializer = ClassSerializer(classes,many=True)
        return Response(serializer.data)


class CourseListView(APIView):
    def get(self , request):
        course=Course.objects.all()
        serializer = CourseSerializer(course,many=True)
        return Response(serializer.data)