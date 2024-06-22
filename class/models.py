from django.db import models

# Create your models here.
class Class(models.Model):
    class_trainer=models.CharField(max_length=20)
    class_prefect=models.CharField(max_length=20)
    number_of_laptops=models.IntegerField()
    color_of_chairs=models.CharField(max_length=20)
    number_of_chairs= models.PositiveSmallIntegerField()
    number_of_tables= models.PositiveSmallIntegerField()
    number_of_boards= models.CharField(max_length=10)
    number_of_students=models.PositiveSmallIntegerField()
    number_of_windows= models.PositiveSmallIntegerField()
    number_of_trainers=models.PositiveSmallIntegerField()


    def __str__(self):
         return f"{self.quantity} {self.sufficient_space}"