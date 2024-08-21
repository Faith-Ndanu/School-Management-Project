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
        country=request.query_params.get("country")
        first_name=request.query_params.get("first_name")
        if country:
            student=student.filter(country=country)
        if first_name:
            student=student.filter(first_name=first_name)

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
    # def enroll_student(self,student,course_id):
    #     course=Course.objects.get(id=course_id)
    #     student.courses.add(course)



    # def post(self,request,id):
    #     student=Student.objects.get(id=id)
    #     action=request.data.get("action")
    #     if action=="enroll":
    #         course_id=request.data.get("course_id")
    #         self.enroll_student(student,course_id)
    #         return Response(status=status.HTTP_202_ACCEPTED)    



    # def get(self,request,id):
    #     student=Student.objects.get(id=id)
    #     serializer=StudentSerializer(student)
    #     return Response(serializer.data)
    

    
    # def put(self,request,id):
    #     student=Student.objects.get(id=id)
    #     serializer=StudentSerializer(student,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    # def delete(self,request,id):
    #     student=Student.objects.get(id=id)
    #     student.delete()    
    #     return Response(status=status.HTTP_202_ACCEPTED)
    def get(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def post(self, request, id):
        student = Student.objects.get(id=id)
        class_id = request.data.get("class_id")
        self.add_student_to_class(student, class_id)
        return Response(status=status.HTTP_202_ACCEPTED)
    def add_student_to_class(self, student, class_id):
        class_instance = Class.objects.get(id=class_id)
        student.classes.add(class_instance)



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
        

    def post(self, request):
        teacher_id = request.data.get("teacher_id")
        course_id = request.data.get("course_id")
        day = request.data.get("day")
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")
        self.create_class_period(teacher_id, course_id, day, start_time, end_time)
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def create_class_period(self, teacher_id, course_id, day, start_time, end_time):
        teacher = Teacher.objects.get(id=teacher_id)
        course = Course.objects.get(id=course_id)
        class_period = ClassPeriod.objects.create(teacher=teacher, course=course, day=day, start_time=start_time, end_time=end_time)
        class_period.save()

class WeeklyTimetableView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data)    


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
    
    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        course_id = request.data.get("course_id")
        class_id = request.data.get("class_id")
        self.assign_teacher_to_course(teacher, course_id)
        self.assign_teacher_to_class(teacher, class_id)
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def assign_teacher_to_course(self, teacher, course_id):
        course = Course.objects.get(id=course_id)
        teacher.courses.add(course)

    def assign_teacher_to_class(self, teacher, class_id):
        class_instance = Class.objects.get(id=class_id)
        teacher.classes.add(class_instance)
































