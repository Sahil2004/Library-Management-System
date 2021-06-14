from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Borrower

def login(request):
    return render(request, 'lib_man/login.html')

def lib_search(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'lib_man/library_search.html', context)

def dashboard(request):
    return render(request, 'lib_man/portalPages/dashboard.html')

def books(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'lib_man/portalPages/books.html', context)
    
def borrowers(request):
    context = {
        'borrowers': Borrower.objects.all()
    }
    return render(request, 'lib_man/portalPages/borrowers.html', context)

def borrowed_books(request):
    return render(request, 'lib_man/portalPages/borrowed_books.html')