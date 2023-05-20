from django.shortcuts import render
from django.http import HttpResponse
from .models import Result,Student
# Create your views here.

def homepage(request):
    return render(request,'dashboard.html',)



def caresultPage(request):
    # cadata=Result.objects.get(studentDetails='1001')
    # context ={
    #     'cadata':cadata
    # }
    return render(request,'caresultpage.html',)

def resultUpload(request):
    if request.method == "POST":
        program=request.POST.get("program")
        stdname=request.POST.get("stdname")
        module=request.POST.get("module")
        result=request.POST.get("result")
        marks=request.POST.get("marks")
        return render(request,print('suncess'))
    else:
       return render(request,'resultupload.html',)
    


def regStudent(request):
    if request.method == "GET":
        print('Testeted ok')
        return render(request,'studentreg.html',)
    else:
         fname=request.POST["fname"]
         lname=request.POST["lname"]
         regnumber=request.POST["regnumber"]
         newstd= Student(firstName=fname,lastName=lname,registrtionNo=regnumber)
         print("passed")
         newstd.save()
         print("passed")
         return render(request,'studentreg.html',)

def regfunc(request):
    if request.method == "POST":
         fname=request.POST["fname"]
         lname=request.POST["lname"]
         regnumber=request.POST["regnumber"]
         newstd= Student(firstName=fname,lastName=lname,registrtionNo=regnumber)
         print("passed")
         newstd.save()
         print("passed")
    return render(request,'studentreg.html',)



def claimpage(request):
    return render(request,'claimpopup.html',)



# upload result students result
def uploadResults(request):
    if request.method == "POST":
        program=request.POST.get("program")
        stdname=request.POST.get("stdname")
        module=request.POST.get("module")
        result=request.POST.get("result")
        marks=request.POST.get("marks")

        return render(request,print('suncess'))
    else:
         return render(request,print('fail'))
