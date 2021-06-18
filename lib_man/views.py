from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Book, Borrower
from .forms import EditBookForm, AddBookForm, DeleteBookForm, LoginForm

def login_page(request):
    context = {
        'login_form': LoginForm()
    }
    return render(request, 'lib_man/login.html', context)

def lib_search(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'lib_man/library_search.html', context)

@login_required(login_url='/lib_man/login')
def dashboard(request):
    context = {
        'no_of_books': Book.objects.all().count(),
        'no_of_borrowed_books': Book.objects.filter(status_borrowed=True).count(),
        'no_of_borrowers': Borrower.objects.all().count()
    }
    return render(request, 'lib_man/portalPages/dashboard.html', context)

@login_required(login_url='/lib_man/login')
def books(request):
    context = {
        'books': Book.objects.all(),
        'edit_book_form': EditBookForm(),
        'add_book_form': AddBookForm(),
        'delete_book_form': DeleteBookForm()
    }
    return render(request, 'lib_man/portalPages/books.html', context)

@login_required(login_url='/lib_man/login')
def borrowers(request):
    context = {
        'borrowers': Borrower.objects.all()
    }
    return render(request, 'lib_man/portalPages/borrowers.html', context)

@login_required(login_url='/lib_man/login')
def borrowed_books(request):
    return render(request, 'lib_man/portalPages/borrowed_books.html')

# Functions

def librarian_login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('librarian/dashboard')
    else:
        return redirect('login/')

def librarian_logout(request):
    logout(request)
    return redirect('login/')

def edit_book(request):
    book = Book.objects.get(pk = request.POST.get('pk'))
    book.title = request.POST.get('title')
    book.author = request.POST.get('author')
    book.isbn = request.POST.get('isbn')
    book.publisher = request.POST.get('publisher')
    book.genre = request.POST.get('genre')
    book.book_location = request.POST.get('book_location')
    if request.POST.get('status_borrowed') == 'on':
        book.status_borrowed = True
    else:
        book.status_borrowed = False
    book.save()
    return redirect('librarian/books')

def add_book(request):
    status_borrowed = True
    if request.POST.get('status_borrowed') == 'on':
        status_borrowed = True
    else:
        status_borrowed = False
    book = Book.objects.create(
        title=request.POST.get('title'),
        author=request.POST.get('author'),
        isbn=request.POST.get('isbn'),
        publisher=request.POST.get('publisher'),
        genre=request.POST.get('genre'),
        book_location=request.POST.get('book_location'),
        status_borrowed=status_borrowed
    )
    return redirect('librarian/books')

def delete_book(request):
    book = Book.objects.get(pk = request.POST.get('pk'))
    book.delete()
    return redirect('librarian/books')