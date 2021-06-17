from django import forms
from .models import Book

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': "username",
            'class': 'form-control'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'id': "password",
            'class': 'form-control'
        }
    ))

class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
    pk = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'style': 'display: none',
            'id': "primary_key"
        }
    ))
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': 'Enter Title',
            'id': "title"
        }
    ))
    author = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': "Enter author's name",
            'id': 'author'
        }
    ))
    isbn = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '13',
            'placeholder': 'Enter ISBN number',
            'id': 'ISBNno'
        }
    ))
    publisher = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': "Enter publisher's name",
            'id': 'pubHouse'
        }
    ))
    genre = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': 'Enter genre',
            'id': 'genre'
        }
    ))
    book_location = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': 'Enter book location',
            'id': 'location'
        }
    ))
    status_borrowed = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-label',
            'id': 'status_borrowed',
        },
    ))

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': 'Enter Title',
            'id': "titleAdd"
        }
    ))
    author = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': "Enter author's name",
            'id': 'authorAdd'
        }
    ))
    isbn = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '13',
            'placeholder': 'Enter ISBN number',
            'id': 'ISBNnoAdd'
        }
    ))
    publisher = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': "Enter publisher's name",
            'id': 'pubHouseAdd'
        }
    ))
    genre = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': 'Enter genre',
            'id': 'genreAdd'
        }
    ))
    book_location = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': 'Enter book location',
            'id': 'locationAdd'
        }
    ))
    status_borrowed = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-label',
            'id': 'status_borrowedAdd',
        },
    ))