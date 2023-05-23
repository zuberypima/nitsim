from django.db import models

# Create your models here.
class ProgramReg(models.Model):
    name =models.CharField(max_length=255,unique=True)
    TYPE =[
        ('Bachelor Degree','Bachelor Degree'),
        ('DIPLOMA','DIPLOMA'),
    ]
    type =models.CharField(max_length=200,choices=TYPE)
    durations=models.CharField(max_length=200)
    semisterNo=models.CharField(max_length=200)

    def __str__(self):
        return self.type+ ' in  '+ self.name

class CourseRegitration(models.Model):
    programName=models.ForeignKey(ProgramReg,on_delete=models.CASCADE)
    courseName=models.CharField(max_length=255,unique=True)
    code=models.CharField(max_length=200, unique=True)
    caMarks=models.CharField(max_length=200)
    finalMarks=models.CharField(max_length=200)

    def __str__(self):
        return self.courseName
    

    #students registration numbers 
class RegNumber(models.Model):
    regNo =models.CharField(unique=True,max_length=255)
    def __str__(self):
        return self.regNo
    

class Student(models.Model):
    firstName =models.CharField(max_length=255)
    lastName =models.CharField(max_length=200) 
    registrtionNo =models.OneToOneField(RegNumber,on_delete=models.CASCADE)
    program=models.ForeignKey(ProgramReg,on_delete=models.CASCADE)
    image =models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.firstName+" "+self.lastName
    

class Result(models.Model):
    program =models.ForeignKey(ProgramReg,on_delete=models.CASCADE)
    course =models.ForeignKey(CourseRegitration, on_delete= models.CASCADE)
    resultTypes=models.CharField(max_length=200)
    marks =models.CharField(max_length=200)
    claim=models.TextField(null=True,blank=True)
    evidenceFile =models.ImageField(blank=True)
    def __str__(self):
        return str(self.studentDetails)
    


class Exam(models.Model):
    programname =models.ForeignKey(ProgramReg, on_delete=models.CASCADE)
    course =models.ForeignKey (CourseRegitration,on_delete=models.CASCADE)
    # modulename =models.CharField(max_length=200) 
    examtype =models.CharField(max_length=255, blank=True)
    # date=models.ForeignKey(ProgramReg,on_delete=models.CASCADE)
    totalmarks =models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.modulename+" "+self.examtype