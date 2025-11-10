from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.detail import DetailView
from .models import Book, Library
# Home view
def home(request):
    return render(request, 'relationship_app/home.html')


# Registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for Library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
# Function-based view to add a book
from .forms import BookForm  # make sure you have a BookForm in forms.py

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})
from django.shortcuts import render
from .models import Library  # Make sure Library model exists

def list_libraries(request):
    libraries = Library.objects.all()  # Get all libraries
    return render(request, 'relationship_app/list_libraries.html', {'libraries': libraries})
from .forms import LibraryForm  # Make sure you have a LibraryForm in forms.py

def add_library(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_libraries')  # After adding, redirect to the list
    else:
        form = LibraryForm()
    return render(request, 'relationship_app/add_library.html', {'form': form})
