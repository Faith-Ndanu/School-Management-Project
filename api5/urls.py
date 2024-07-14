from django.urls import path
from .views import Course


urlpatterns=[
    path("course/",Course.as_view(),name="course_list_view")
]






