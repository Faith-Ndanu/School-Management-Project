from django.urls import path
from .views import Teacher


urlpatterns=[
    path("teacher/",Teacher.as_view(),name="teacher_list_view")
]