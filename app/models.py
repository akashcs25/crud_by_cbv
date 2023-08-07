from django.db import models

# Create your models here.
class School(models.Model):
    SCHname=models.CharField(max_length=100)
    SCHprinci=models.CharField(max_length=100)
    SCHloc=models.CharField(max_length=100)

    def __str__(self):
        return self.SCHname

class Student(models.Model):
    Sname=models.CharField(max_length=100)
    Sage=models.IntegerField()
    SCHname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='panda')

    def __str__(self):
        return self.Sname