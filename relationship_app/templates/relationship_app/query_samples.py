# relationship_app/query_samples.py

from .models import Book, Library, Author, Librarian

def list_all_books_in_library(library_id):
    """
    Returns a QuerySet of all Book objects in a library specified by its id.
    """
    return Book.objects.filter(library_id=library_id)

def list_all_books_in_library_by_obj(library_obj):
    """
    Alternative: accepts a Library instance and returns its books.
    """
    return Book.objects.filter(library=library_obj)

def query_all_books_by_author(author_id):
    """
    Returns a QuerySet of all Book objects by a specific author id.
    """
    return Book.objects.filter(author_id=author_id)

def query_all_books_by_author_obj(author_obj):
    """
    Alternative: accepts an Author instance and returns its books.
    """
    return Book.objects.filter(author=author_obj)

def retrieve_librarian_for_library(library_id):
    """
    Returns the Librarian instance for a given library id.
    """
    lib = Library.objects.get(id=library_id)
    return lib.librarian

def retrieve_librarian_for_library_by_obj(library_obj):
    """
    Accepts a Library object and returns its librarian.
    """
    return library_obj.librarian
