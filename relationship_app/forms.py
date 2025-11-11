from django import forms
from .models import Book, Library

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'library']

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['name', 'address']
