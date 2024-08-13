from django.db import models

# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    country= models.CharField(max_length=20)
    date_of_birth= models.DateField()
    student_code = models.PositiveSmallIntegerField()
    student_bio = models.TextField(null=True)
    enrollment_year = models.IntegerField(null=True)
    # courses=models.ManyToManyField(courses)
   


    def __str__(self):
         return f"{self.first_name} {self.last_name}"


   



















