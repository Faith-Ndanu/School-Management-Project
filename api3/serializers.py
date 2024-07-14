from rest_framework import serializers
from teacher.models import Teacher

class Teacher(serializers.ModelSerializer):
    class Meta:
        model=  Teacher
        fields="__all__"