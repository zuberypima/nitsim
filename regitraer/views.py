from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,ProgramReg,Student
from .forms import PrograMform,CourseRegForm,StudentRegForm
# Create your views here.


def add_program(request):
    if request.method == 'POST':
        form = PrograMform(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('book-list')
            print('Successfully')
    else:
        form = PrograMform()
    return render(request, 'programreg.html', {'form': form})


def add_course(request):
    if request.method == 'POST':
        form = CourseRegForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('book-list')
            print('Successfully')
    else:
        form = CourseRegForm()
    return render(request, 'coursereg.html', {'form': form})



def add_student(request):
    if request.method == 'POST':
        form = StudentRegForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('book-list')
            print('Successfully')
    else:
        form = StudentRegForm()
    return render(request, 'studentsregister.html', {'form': form})




def student_list(request):
    return render (request, 'studentlist.html')


def registerdash(request):
    return render (request, 'admindash.html')

def studentdahs(request):
    return render (request, 'studentdash.html')