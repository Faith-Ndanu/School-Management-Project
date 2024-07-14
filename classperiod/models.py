from django.db import models

# Create your models here.from django.db import models

class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course=models.CharField(max_length=20)
    classroom=models.CharField(max_length=20)
    day_of_week = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.course} {self.day_of_week}"



