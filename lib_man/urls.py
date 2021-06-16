from django.conf import settings
from django.urls import path
from  . import views
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.login, name="login"),
    path('library_search/', views.lib_search, name="lib_search"),
    path('admin/dashboard', views.dashboard, name="dashboard"),
    path('admin/books', views.books, name="books"),
    path('admin/borrowers', views.borrowers, name="borrowers"),
    path('admin/borrowed_books', views.borrowed_books, name="borrowed_books"),

    path('edit_book', views.edit_book, name="edit_book"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)