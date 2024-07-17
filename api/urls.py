from django.urls import path
from .views import StudentListView
from .views import Course
from .views import Class
from .views import Teacher
from .views import ClassPeriodListView


urlpatterns=[
    path("classperiods/",ClassPeriodListView.as_view(),name="classperiods_list_view")
]


urlpatterns=[
    path("teacher/",Teacher.as_view(),name="teacher_list_view")
]

urlpatterns=[
    path("students/",StudentListView.as_view(),name="student_list_view")
]

urlpatterns=[
    path("course/",Course.as_view(),name="course_list_view")
]

urlpatterns=[
    path("classes/",Class.as_view(),name="classes_list_view")
]

