from django.db import models
from regitraer.models import ProgramReg,CourseRegitration
from regitraer.models import ProgramReg,Student,RegNumber
# Create your models here.



class Result(models.Model):
    def __str__(self):
        return str('')
    

class Exam(models.Model):
    programName= models.ForeignKey(ProgramReg, on_delete=models.CASCADE,max_length=255)
    moduleCode =models.CharField(max_length=255)
    totalMarks =models.CharField(max_length=255)
    examType =models.CharField(max_length=255)
    def __str__(self):
        return self.moduleCode+" "+self.examType
    

class CaResult(models.Model):
    registrationNo =models.ForeignKey(RegNumber, on_delete=models.CASCADE)
    moduleName=models.ForeignKey(CourseRegitration,on_delete=models.CASCADE)
    test_1=models.CharField(max_length=255)
    test_2=models.CharField(max_length=255)
    quize_1=models.CharField(max_length=255)
    quize_2=models.CharField(max_length=255)
    attendance=models.CharField(max_length=255)

    def __str__(self):
       return self.registrationNo