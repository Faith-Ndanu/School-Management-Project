from django.db import models

# Create your models here.
class Course(models.Model):
    course_title=models.CharField(max_length=20)
    course_code = models.PositiveSmallIntegerField()
    number_of_units=models.IntegerField()
    number_of_students=models.IntegerField()
    career_outcome= models.CharField(max_length=20)
    scheduled_time=models.IntegerField()
    assessments= models.CharField(max_length=10)
    practical_application=models.CharField(max_length=20)
    clear_description= models.CharField(max_length=20)
    course_period=models.PositiveSmallIntegerField()


    def __str__(self):
         return f"{self.title} {self.code}"
    




    