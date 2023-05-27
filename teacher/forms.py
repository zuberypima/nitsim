from django import forms
from .models import Exam



class ExamRegForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['programName','moduleCode','totalMarks','examType',]