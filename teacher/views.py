from django.shortcuts import render
from .models import Exam,CaResult
from .forms import ExamRegForm,CaResultForm
# Create your views here.



def add_exam(request):
    if request.method == 'POST':
        form = ExamRegForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('book-list')
    else:
        form = ExamRegForm()
    return render(request, 'examregister.html', {'form': form})



def add_caresults(request):
    if request.method == 'POST':
        form = CaResultForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('book-list')
    else:
        form = CaResultForm()
    return render(request, 'addcaresult.html', {'form': form})


def update_caresults(request,pk):
    result =CaResult.objects.get(id=pk)
    form = CaResultForm(instance=result)
    if request.method == 'POST':
        form = CaResultForm(request.POST,instance=result)
        if form.is_valid():
            form.save()
            # return redirect('book-list')
    else:
        form = CaResultForm()
    return render(request, 'addcaresult.html', {'form': form})



def  teacherdashboard(request):
    return render (request, 'teacherdash.html')

def  results(request):
    return render (request, 'allresults.html')

def  ca_results(request):
    caresults =CaResult.objects.all()
    return render (request, 'ca_results.html',{'caresults':caresults})
