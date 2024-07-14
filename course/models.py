import datetime
from django.db import models

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=20)
    code = models.PositiveSmallIntegerField()
    number_of_units=models.IntegerField(default=0)
    scheduled_time = models.DateTimeField(default=datetime.datetime(2024, 7, 12, 14, 30, 0))
    number_of_students=models.IntegerField(default=0)
    career_outcome= models.CharField(max_length=20)
    assessments= models.CharField(max_length=10)
    practical_application=models.CharField(max_length=20)
    clear_description= models.CharField(max_length=20)
    course_period=models.PositiveSmallIntegerField()
    


    def __str__(self):
         return f"{self.title} {self.code}"
    




    