from rest_framework import serializers
from student.models import ClassPeriod

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassPeriod
        fields="__all__"

        