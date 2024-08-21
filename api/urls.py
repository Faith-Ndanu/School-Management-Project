from django.urls import path
from .views import StudentListView
from .views import CourseListView
from .views import ClassListView
from .views import TeacherListView
from .views import ClassPeriodListView
from .views import StudentDetailView
from .views import TeacherDetailView
from .views import CourseDetailView
# from .views import ClassPeriodDetailView
from .views import ClassDetailView
from .views import WeeklyTimetableView
urlpatterns = [
    path('student/', StudentListView.as_view(), name='student_list_view'),
    path('courses/', CourseListView.as_view(), name='courses_list_view'),
    path('classes/', ClassListView.as_view(), name='classes_list_view'),
    path('teacher/', TeacherListView.as_view(), name='teacher_list_view'),
    path('classperiod/', ClassPeriodListView.as_view(), name='classperiod_list_view'),
    path('student/<int:id>/', StudentDetailView.as_view(), name='student_detail_view'),
    path('teacher/<int:id>/', TeacherDetailView.as_view(), name='teacher_detail_view'),
    path('classes/<int:id>/', ClassDetailView.as_view(), name='classes_detail_view'),
    # path('classperiod/<int:id>/', ClassPeriodDetailView.as_view(), name='classperiod_detail_view'),
    path('courses/<int:id>/', CourseDetailView.as_view(), name='courses_detail_view'),
    path('student/<int:id>/add_to_class/', StudentDetailView.as_view(), name='add_student_to_class'),
    path('teacher/<int:id>/assign/', TeacherDetailView.as_view(), name='assign_teacher'),
    path('classperiod/create/', ClassPeriodListView.as_view(), name='create_class_period'),
    path('timetable/', WeeklyTimetableView.as_view(), name='weekly_timetable'),
]






# from django.urls import path
# from .views import StudentListView
# from .views import CourseListView
# from .views import ClassListView
# from .views import TeacherListView
# from .views import ClassPeriodListView
# from .views import StudentDetailView
# from .views import ClassDetailView
# from .views import ClassPeriodDetailView
# from .views import TeacherDetailView
# from .views import CourseDetailView


# urlpatterns=[
#     path("classperiods/",ClassPeriodListView.as_view(),name="classperiods_list_view"),
#     path("teacher/",TeacherListView.as_view(),name="teacher_list_view"),
#     path("student/",StudentListView.as_view(),name="student_list_view"),
#     path("classes/",ClassListView.as_view(),name="classes_list_view"),
#     path("course/",CourseListView.as_view(),name="course_list_view"),
#     path("student/<int:id>/",StudentDetailView.as_view(),name="student_detail_view"),
#     path("classes/<int:id>/",ClassDetailView.as_view(),name="classes_detail_view"),
#     path("teacher/<int:id>/",TeacherDetailView.as_view(),name="teacher_detail_view"),
#     path("course/<int:id>/",CourseDetailView.as_view(),name="course_detail_view"),
#     path("classperiod/<int:id>/",ClassPeriodDetailView.as_view(),name="classperiod_detail_view")


# ]



