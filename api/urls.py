from django.urls import path
from .views import StudentListView
from .views import CourseListView
from .views import ClassListView
from .views import TeacherListView
from .views import ClassPeriodListView


urlpatterns=[
    path("classperiods/",ClassPeriodListView.as_view(),name="classperiods_list_view"),
    path("teacher/",TeacherListView.as_view(),name="teacher_list_view"),
    path("students/",StudentListView.as_view(),name="student_list_view"),
    path("classes/",ClassListView.as_view(),name="classes_list_view"),
    path("course/",CourseListView.as_view(),name="course_list_view")

]



