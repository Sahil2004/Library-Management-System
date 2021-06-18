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
            'id': "primaryKeyEdit"
        }
    ))
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': 'Enter Title',
            'id': 'titleEdit'
        }
    ))
    author = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': "Enter author's name",
            'id': 'authorEdit'
        }
    ))
    isbn = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '13',
            'placeholder': 'Enter ISBN number',
            'id': 'isbnNoEdit'
        }
    ))
    publisher = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': "Enter publisher's name",
            'id': 'pubHouseEdit'
        }
    ))
    genre = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': 'Enter genre',
            'id': 'genreEdit'
        }
    ))
    book_location = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': 'Enter book location',
            'id': 'bookLocationEdit'
        }
    ))
    status_borrowed = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-label',
            'id': 'statusBorrowedEdit',
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
            'id': 'bookLocationAdd'
        }
    ))
    status_borrowed = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-label',
            'id': 'statusBorrowedAdd',
        },
    ))

class DeleteBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
    pk = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'style': 'display: none',
            'id': "primaryKeyDel"
        }
    ))