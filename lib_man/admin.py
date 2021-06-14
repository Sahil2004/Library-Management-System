from django.contrib import admin
from .models import Book, Borrower

# Register your models here.
admin.site.register(Book)
admin.site.register(Borrower)