from django.conf import settings
from django.urls import path
from  . import views
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.login_page, name="login_page"),
    path('library_search/', views.lib_search, name="lib_search"),
    path('librarian/dashboard', views.dashboard, name="dashboard"),
    path('librarian/books', views.books, name="books"),
    path('librarian/borrowers', views.borrowers, name="borrowers"),
    path('librarian/borrowed_books', views.borrowed_books, name="borrowed_books"),

    path('librarian_login', views.librarian_login, name="librarian_login"),
    path('librarian_logout', views.librarian_logout, name="librarian_logout"),
    path('edit_book', views.edit_book, name="edit_book"),
    path('add_book', views.add_book, name="add_book"),
    path('delete_book', views.delete_book, name="delete_book"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)