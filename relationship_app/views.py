from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Book, Library
from .forms import BookForm, LibraryForm

# Home
def home(request):
    return render(request, 'relationship_app/home.html')

# BOOKS
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# LIBRARIES
def list_libraries(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/list_libraries.html', {'libraries': libraries})

def add_library(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_libraries')
    else:
        form = LibraryForm()
    return render(request, 'relationship_app/add_library.html', {'form': form})

# CLASS-BASED VIEW for library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
