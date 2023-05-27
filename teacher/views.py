from django.shortcuts import render
from .models import Exam
from .forms import ExamRegForm
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


def  teacherdashboard(request):
    return render (request, 'teacherdash.html')