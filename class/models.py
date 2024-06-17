from django.db import models

# Create your models here.
class Class(models.Model):
    quantity=models.PositiveSmallIntegerField()
    sufficient_space = models.CharField(max_length=20)
    learning_models = models.PositiveSmallIntegerField()
    educational_resources= models.CharField(max_length=20)
    chairs= models.PositiveSmallIntegerField()
    tables= models.PositiveSmallIntegerField()
    board= models.CharField(max_length=10)
    students=models.PositiveSmallIntegerField(max_length=50)
    windows= models.PositiveSmallIntegerField()
    trainers=models.PositiveSmallIntegerField(max_length=20)


    def __str__(self):
         return f"{self.quantity} {self.sufficient_space}"