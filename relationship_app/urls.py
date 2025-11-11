from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('libraries/', views.list_libraries, name='list_libraries'),
    path('libraries/add/', views.add_library, name='add_library'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
