from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
from .models import Book, Borrower
from .forms import EditBookForm, AddBookForm, DeleteBookForm, LoginForm, SearchBooksForm, SearchBooksUnauthForm
from .forms import EditBorrowerForm, SearchBorrowersForm, AddBorrowerForm, DeleteBorrowerForm
from datetime import datetime



def search_books_results(keyword, search_by):
    if search_by == 'Book Title':
        return Book.objects.filter(Q(title__icontains=keyword))
    if search_by == 'Book Author':
        return Book.objects.filter(Q(author__icontains=keyword))
    if search_by == 'ISBN Number':
        return Book.objects.filter(Q(isbn__icontains=keyword))
    if search_by == 'Publishing House':
        return Book.objects.filter(Q(publisher__icontains=keyword))
    if search_by == 'Genre':
        return Book.objects.filter(Q(genre__icontains=keyword))
    if search_by == 'Book Location':
        return Book.objects.filter(Q(book_location__icontains=keyword))
    if search_by == 'Status':
        if not keyword.upper() == 'AVAILABLE' and not keyword.upper() == 'BORROWED':
            return Book.objects.none()
        else:
            status = keyword.upper() == 'BORROWED'
            return Book.objects.filter(status_borrowed=status)

def search_borrowers_results(keyword, search_by):
    if search_by == 'Name':
        return Borrower.objects.filter(Q(name__icontains=keyword))
    if search_by == 'Admission Number':
        return Borrower.objects.filter(Q(adm_no__icontains=keyword))
    if search_by == 'Grade':
        return Borrower.objects.filter(Q(grade=keyword))
    if search_by == 'Section':
        return Borrower.objects.filter(Q(section=keyword))
    if search_by == 'Roll Number':
        return Borrower.objects.filter(Q(roll_no=keyword))
    if search_by == 'Contact Number':
        return Borrower.ojects.filter(Q(contact_no__icontains=keyword))
    if search_by == 'Book Borrowed':
        return Borrower.objects.filter(Q(book_borrowed__title__icontains=keyword))
    if search_by == 'Date Borrowed': 
        date_to_search = datetime.strptime(keyword, '%b %d %Y')
        return Borrower.objects.filter(Q(date_borrowed__contains= datetime.date(date_to_search))) 
    if search_by == 'Date Due': 
        date_to_search = datetime.strptime(keyword, '%b %d %Y')
        return Borrower.objects.filter(Q(date_due__contains = datetime.date(date_to_search)))       
    


# Pages

def login(request):
    context = {
        'login_form': LoginForm()
    }
    return render(request, 'lib_man/login.html', context)



def lib_search(request):
    if not request.GET:
        context = {
            'books': Book.objects.all(),
            'search_books_unauth_form': SearchBooksUnauthForm()
        }
    else:
        context = {
            'books': search_books_results(request.GET.get('keyword'), request.GET.get('search_by')),
            'search_books_unauth_form': SearchBooksUnauthForm(),
            'search_results_present': True
        }
    return render(request, 'lib_man/library_search.html', context)



@login_required(login_url='login')
def dashboard(request):
    context = {
        'no_of_books': Book.objects.all().count(),
        'no_of_borrowed_books': Book.objects.filter(status_borrowed=True).count(),
        'no_of_borrowers': Borrower.objects.all().count(), 
        'no_of_books_due': Borrower.objects.filter(date_due__lte = datetime.today()).count()
    }
    return render(request, 'lib_man/portalPages/dashboard.html', context)


@login_required(login_url='login')
def books(request):
    context = {}
    if not request.GET:
        context = {
            'books': Book.objects.all(),
            'edit_book_form': EditBookForm(),
            'add_book_form': AddBookForm(),
            'delete_book_form': DeleteBookForm(),
            'search_books_form': SearchBooksForm()
        }
    else:
        context = {
            'books': search_books_results(request.GET.get('keyword'), request.GET.get('search_by')),
            'edit_book_form': EditBookForm(),
            'add_book_form': AddBookForm(),
            'delete_book_form': DeleteBookForm(),
            'search_books_form': SearchBooksForm()
        }

    return render(request, 'lib_man/portalPages/books.html', context)


@login_required(login_url='login')
def borrowers(request):
    context = {}
    if not request.GET:
        context = {
            'borrowers': Borrower.objects.all(),
            'edit_borrower_form': EditBorrowerForm(),
            'add_borrower_form': AddBorrowerForm(),
            'delete_borrower_form': DeleteBorrowerForm, 
            'books': Book.objects.filter(status_borrowed=False),  
            'search_borrowers_form': SearchBorrowersForm()
        
        }
    else:
        context = {
            'borrowers': search_borrowers_results(request.GET.get('keyword'), request.GET.get('search_by')),
            'edit_borrower_form': EditBorrowerForm(),
            'add_borrower_form': AddBorrowerForm(),
            'delete_borrower_form': DeleteBorrowerForm, 
            'search_borrowers_form': SearchBorrowersForm(), 
            'books': Book.objects.filter(status_borrowed=False) 
       }

    return render(request, 'lib_man/portalPages/borrowers.html', context)




@login_required(login_url='login')
def borrowed_books(request):
    return render(request, 'lib_man/portalPages/borrowed_books.html')

# App functions

#Book App Functions

def librarian_login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login_user(request, user)
        return redirect('dashboard')
    else:
        context = {
            'login_form': LoginForm(),
            'login_error': True
        }
        return render(request, 'lib_man/login.html', context)

def librarian_logout(request):
    logout_user(request)
    return redirect('login')

def edit_book(request):
    book = Book.objects.get(pk = request.POST.get('pk'))
    book.title = request.POST.get('title')
    book.author = request.POST.get('author')
    book.isbn = request.POST.get('isbn')
    book.publisher = request.POST.get('publisher')
    book.genre = request.POST.get('genre')
    book.book_location = request.POST.get('book_location')
    book.save()
    return redirect('books')

def add_book(request):
    Book.objects.create(
    title=request.POST.get('title'),
    author=request.POST.get('author'),
    isbn=request.POST.get('isbn'),
    publisher=request.POST.get('publisher'),
    genre=request.POST.get('genre'),
    book_location=request.POST.get('book_location'),
    status_borrowed = False
    )
    return redirect('books')

def delete_book(request):
    book = Book.objects.get(pk = request.POST.get('pk'))
    book.delete()
    return redirect('books')

def search_books(request):
    base_url = reverse('books')
    query_string =  urlencode({'search_by': request.POST.get('search_by'), 'keyword': request.POST.get('keyword')})
    url = '{}?{}'.format(base_url, query_string)
    return redirect(url)

def search_books_unauth(request):
    base_url = reverse('lib_search')
    query_string =  urlencode({'search_by': request.POST.get('search_by'), 'keyword': request.POST.get('keyword')})
    url = '{}?{}'.format(base_url, query_string)
    return redirect(url)

#Borrower App Functions

def search_borrowers(request):
    base_url = reverse('borrowers')
    query_string =  urlencode({'search_by': request.POST.get('search_by'), 'keyword': request.POST.get('keyword')})
    url = '{}?{}'.format(base_url, query_string)
    return redirect(url)
    

def edit_borrower(request):
    borrower = Borrower.objects.get(pk = request.POST.get('pk'))
    borrower.name = request.POST.get('name')
    borrower.adm_no = request.POST.get('adm_no')
    borrower.grade = request.POST.get('grade')
    borrower.section = request.POST.get('section')
    borrower.roll_no = request.POST.get('roll_no')
    old_book_pk = borrower.book_borrowed.pk
    old_book = Book.objects.get(pk = old_book_pk)
    old_book.status_borrowed = False
    old_book.save()
    new_book = Book.objects.get(pk = request.POST.get('book_pk'))
    borrower.book_borrowed = new_book
    new_book.status_borrowed = True
    new_book.save()
    borrower.save()
    return redirect('borrowers')    

def delete_borrower(request):
    borrower = Borrower.objects.get(pk = request.POST.get('pk'))
    current_book_pk = borrower.book_borrowed.pk
    current_book = Book.objects.get(pk=current_book_pk)
    current_book.status_borrowed = False
    current_book.save() 
    borrower.delete()
    return redirect('borrowers')

def add_borrower(request):
    book_to_add =Book.objects.get(pk = request.POST.get('book_pk'))     
    Borrower.objects.create(
    name = request.POST.get('name'),
    adm_no = request.POST.get('adm_no'),
    section = request.POST.get('section'),
    roll_no =request.POST.get('roll_no'),
    contact_no = request.POST.get('contact_no'), 
    grade=request.POST.get('grade'),
    book_borrowed = book_to_add,
    date_borrowed = request.POST.get('date_borrowed'), 
    date_due = request.POST.get('date_due')
    )
    book_to_add.status_borrowed = True
    book_to_add.save()
    return redirect('borrowers')