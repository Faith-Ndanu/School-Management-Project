from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    nationality= models.CharField(max_length=20)
    teacher_resume=models.CharField(max_length=20)
    years_of_experience= models.PositiveSmallIntegerField()
    office_number=models.PositiveSmallIntegerField()
    date_of_employment= models.DateField()
    phone_number=models.CharField(max_length=20)


    def __str__(self):
         return f"{self.first_name} {self.last_name}"
















