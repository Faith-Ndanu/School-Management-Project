from django.db import models

# Create your models here.
class Class(models.Model):
    class_trainer=models.CharField(max_length=20)
    class_prefect=models.CharField(max_length=20)
    number_of_laptops=models.IntegerField(default=0)
    color_of_chairs = models.CharField(max_length=255, default='DefaultColor')
    number_of_chairs= models.PositiveSmallIntegerField(default=0)
    number_of_tables= models.PositiveSmallIntegerField(default=0)
    number_of_boards= models.PositiveSmallIntegerField(default=0)
    number_of_students=models.IntegerField(default=0)
    number_of_windows= models.PositiveSmallIntegerField(default=0)
    number_of_trainers=models.PositiveSmallIntegerField(default=0)


    def __str__(self):
         return f"{self.class_prefect} {self.class_trainer}"
    

    