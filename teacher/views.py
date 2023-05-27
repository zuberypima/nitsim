from django.shortcuts import render

# Create your views here.



def add_exam(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})