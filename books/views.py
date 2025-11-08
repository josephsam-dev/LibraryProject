from django.shortcuts import render
from django.http import HttpResponse

# View for /books/
def list_books(request):
    return render(request, 'relationship_app/list_books.html')

# Optional home view for root URL
def home(request):
    return HttpResponse("Welcome to the Library Project!")
