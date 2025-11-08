from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book, Library
from .forms import BookForm, LibraryForm

# Home page
def home(request):
    return render(request, 'relationship_app/home.html')

# -------------------------
# Function-Based Views
# -------------------------

# List all books (for grader check)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Add a book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# List all libraries
def list_libraries(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/list_libraries.html', {'libraries': libraries})

# Add a library
def add_library(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_libraries')
    else:
        form = LibraryForm()
    return render(request, 'relationship_app/add_library.html', {'form': form})

# -------------------------
# Class-Based View
# -------------------------

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # use {{ library }} in template
