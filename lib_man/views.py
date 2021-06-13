from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'lib_man/login.html')

def lib_search(request):
    return HttpResponse("<div>Library Search</div>")

def portal(request):
    return HttpResponse("<div>Portal</div>")

def dashboard(request):
    return HttpResponse("<div>Dashboard</div>")

def books(request):
    return HttpResponse("<div>Books</div>")
    
def borrowers(request):
    return HttpResponse("<div>Borrowers</div>")

def borrowed_books(request):
    return HttpResponse("<div>Borrowers</div>")