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
from rest_framework import status
from rest_framework.response import Response

#Student
class StudentListView(APIView):
    def get(self , request):
        student=Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get(self,request,id):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self,request,id):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        student=Student.objects.get(id=id)
        student.delete()    
        return Response(status=status.HTTP_202_ACCEPTED)

#ClassPeriod
class ClassPeriodListView(APIView):
    def get(self , request):
        classperiod=ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ClassPeriodDetailView(APIView):
    def get(self,request,id):
        classperiod=ClassPeriod.objects.get(id=id)
        serializer=ClassPeriodSerializer(classperiod)
        return Response(serializer.data)
    
    def put(self,request,id):
        classperiod=ClassPeriod.objects.get(id=id)
        serializer=ClassPeriodSerializer(classperiod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        classperiod=ClassPeriod.objects.get(id=id)
        classperiod.delete()    
        return Response(status=status.HTTP_202_ACCEPTED)



#Class
class ClassListView(APIView):
    def get(self , request):
        classes=Class.objects.all()
        serializer = ClassSerializer(classes,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ClassDetailView(APIView):
    def get(self,request,id):
        classes =Class.objects.get(id=id)
        serializer=ClassSerializer(classes)
        return Response(serializer.data)
    
    def put(self,request,id):
        classes=ClassPeriod.objects.get(id=id)
        serializer=ClassSerializer(classes,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        classes=ClassPeriod.objects.get(id=id)
        classes.delete()    
        return Response(status=status.HTTP_202_ACCEPTED)

    




#Course
class CourseListView(APIView):
    def get(self , request):
        course=Course.objects.all()
        serializer = CourseSerializer(course,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):
    def get(self,request,id):
        course=Course.objects.get(id=id)
        serializer=ClassPeriodSerializer(course)
        return Response(serializer.data)
    
    def put(self,request,id):
        course=Course.objects.get(id=id)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        course=Course.objects.get(id=id)
        course.delete()    
        return Response(status=status.HTTP_202_ACCEPTED)

    
#Teacher
class TeacherListView(APIView):
    def get(self , request):
        teacher=Teacher.objects.all()
        serializer = TeacherSerializer(teacher,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer=TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self,request,id):
        teacher=ClassPeriod.objects.get(id=id)
        serializer=TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        teacher=Teacher.objects.get(id=id)
        teacher.delete()    
        return Response(status=status.HTTP_202_ACCEPTED)
































