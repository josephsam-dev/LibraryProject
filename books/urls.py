from django.urls import path
from .views import list_books, home  # import the views you defined

urlpatterns = [
    path('', list_books, name='list_books'),  # maps /books/ to list_books view
    path('home/', home, name='home'),         # optional: /books/home/ goes to home view
]
