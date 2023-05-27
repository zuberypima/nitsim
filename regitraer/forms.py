from django import forms
from .models import ProgramReg,CourseRegitration,Student



class PrograMform(forms.ModelForm):
    class Meta:
        model = ProgramReg
        fields = ['name','type','durations','semisterNo',]



class CourseRegForm(forms.ModelForm):
    class Meta:
        model = CourseRegitration
        fields = ['programName','courseName','code','caMarks','finalMarks']



class StudentRegForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstName','lastName','registrtionNo','program','image']
