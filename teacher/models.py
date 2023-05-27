from django.db import models
from regitraer.models import ProgramReg,CourseRegitration
# Create your models here.



class Result(models.Model):
    def __str__(self):
        return str('')
    

class Exam(models.Model):
    program= models.CharField(max_length=255 )
    modulecode =models.CharField(max_length=255)
    totalmarks =models.CharField(max_length=255)
    examtype =models.CharField(max_length=255)
    def __str__(self):
        return self.modulecode+" "+self.examtype