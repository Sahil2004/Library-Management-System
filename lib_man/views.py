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
    return render(request, 'lib_man/dashboard.html')

def books(request):
    context = {
        'books': Book.objects.all()
    }
    return HttpResponse("<div>Books</div>", context)
    
def borrowers(request):
    context = {
        'borrowers': Borrower.objects.all()
    }
    return HttpResponse("<div>Borrowers</div>", context)

def borrowed_books(request):
    return HttpResponse("<div>Borrowers</div>")