from django.db import models

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=20)
    code = models.PositiveSmallIntegerField()
    learning_objective = models.CharField(max_length=20)
    teaching_method= models.CharField(max_length=20)
    career_outcome= models.CharField(max_length=20)
    course_materials= models.PositiveSmallIntegerField()
    assessments= models.CharField(max_length=10)
    practical_application=models.CharField(max_length=20)
    clear_description= models.CharField(max_length=20)
    course_period=models.PositiveSmallIntegerField()


    def __str__(self):
         return f"{self.title} {self.code}"