from django.contrib import admin
from  .models import Student,CourseRegitration,ProgramReg,Result
# Register your models here.

admin.site.register(ProgramReg)
admin.site.register(CourseRegitration)
admin.site.register(Student)
admin.site.register(Result)

