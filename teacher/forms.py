from django import forms
from .models import Exam,CaResult



class ExamRegForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['programName','moduleCode','totalMarks','examType',]



class CaResultForm(forms.ModelForm):
    class Meta:
        model = CaResult
        fields = ['registrationNo','moduleName','test_1','test_2','quize_1','quize_2','attendance']