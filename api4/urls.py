from django.urls import path
from .views import Class


urlpatterns=[
    path("classes/",Class.as_view(),name="classes_list_view")
]