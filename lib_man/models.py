from django.db import models 
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta

class Book(models.Model):

    def __str__(self):
        return self.title
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    book_location = models.CharField(max_length=50)
    status_borrowed = models.BooleanField(default=False)

class Borrower(models.Model):

    def get_due_date():
        return datetime.today() + timedelta(days=15)

    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    adm_no = models.CharField(max_length=10)
    _class = models.IntegerField(
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ]
    )
    section = models.CharField(max_length=1)
    roll_no = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    contact_no = models.BigIntegerField(
        validators=[
            MaxValueValidator(9999999999),
            MinValueValidator(1111111111)
        ]
    )
    
    book_borrowed = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_borrowed = models.DateField(default=datetime.today)
    date_due = models.DateField(default=get_due_date())
