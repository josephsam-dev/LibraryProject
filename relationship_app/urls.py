from django.urls import path
from . import views
from .views import LibraryDetailView  # import the class-based view

urlpatterns = [
    path('', views.home, name='home'),
    # Books
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),
    # Libraries
    path('libraries/', views.list_libraries, name='list_libraries'),
    path('libraries/add/', views.add_library, name='add_library'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # <-- important
]
