from django import forms
from django.forms.fields import MultipleChoiceField
from .models import Book
from .models import Borrower

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

class SearchBooksForm(forms.Form):
    keyword = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': 'Search',
            'aria-label': 'Search',
            'aria-describedby': 'basic-addon2',
            'tabindex': '1',
            'required': ''
        }
    ))
    search_by = forms.ChoiceField(
        choices=((
            ('Book Title', 'Book Title'), 
            ('Book Author', 'Book Author'),
            ('ISBN Number', 'ISBN Number'),
            ('Publishing House', 'Publishing House'), 
            ('Genre', 'Genre'), 
            ('Book Location', 'Book Location'), 
            ('Status', 'Status'),
        )),
        widget = forms.Select(
            attrs={
                'class':'form-select',
                'style': 'max-width: 20%;'
            }
        )
    )


#Borrower Forms    
class EditBorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = '__all__'
    pk = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'style': 'display: none',
            'id': "primaryKeyEdit"
        }
    ))
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': "Enter borrower's name",
            'id': 'nameEdit'
        }
    ))
    adm_no = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '10',
            'placeholder': "Enter borrower's admission number: ",
            'id': 'admEdit'
        }
    ))
    _class = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'maxlength': '2',
            'placeholder': "Enter borrower's class: ",
            'id': '_classEdit'
        }
    ))
    section = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '1',
            'placeholder': "Enter borrower's section",
            'id': 'sectionEdit'
        }
    ))
    roll_no = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'maxlength': '1',
            'placeholder': "Enter borrower's roll number: ",
            'id': 'rollEdit'
        }
    ))
    contact_no = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'minlength': '1111111111',
            'maxlength': '9999999999',
            'placeholder': "Enter borrower's contact number",
            'id': 'contactEdit'
        }
    ))

    book_borrowed = forms.CharField(label = 'Book Borrowed',
        widget = forms.Select(choices = Book.objects.all()) 
    )


    




    