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

    book_pk = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'style': 'display: none',
            'id': "bookPrimaryKeyEdit"
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
            'placeholder': "Enter borrower's admission number",
            'id': 'admEdit'
        }
    ))
    grade = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'maxlength': '2',
            'placeholder': "Enter borrower's grade",
            'id': 'gradeEdit'
        }
    ))
    section = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': "Enter borrower's section",
            'id': 'sectionEdit'
        }
    ))
    roll_no = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'maxlength': '1',
            'placeholder': "Enter borrower's roll number",
            'id': 'rollEdit'
        }
    ))
    contact_no = forms.IntegerField(widget=forms.TextInput(
        attrs={
            
            'class': 'form-control',
            'minlength': '-9223372036854775808',
            'maxlength': '9223372036854775807',
            'placeholder': "Enter borrower's contact number",
            'id': 'contactEdit'
        }
    ))
    book_borrowed = forms.CharField(widget=forms.TextInput(
        attrs={
            
            'class': 'form-control',
            'placeholder': "Search Book's Title",
            'id': 'bookBorrowedEdit', 
            'autocomplete': 'off', 
            'type': 'text', 
            'onkeyup':"dynamicSearch();displaySearchElems()", 
            'title' : "Type in a name"

        }
    ))

    

class SearchBorrowersForm(forms.Form):
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
            ('Name', 'Name'), 
            ('Admission Number','Admission Number'),
            ('Grade','Grade'),
            ('Section','Section'), 
            ('Roll Number','Roll Number'), 
            ('Contact Number','Contact Number'), 
            ('Book Borrowed','Book Borrowed'),
            ('Date Borrowed','Date Borrowed'),
            ('Date Due','Date Due')
        )),
        widget = forms.Select(
            attrs={
                'class':'form-select',
                'style': 'max-width: 20%;'
            }
        )
    )

    
class AddBorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = '__all__'
    
    book_pk = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'style': 'display: none',
            'id': "bookPrimaryKeyAdd"
        }
    ))    
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': "Enter borrower's name",
            'id': "nameAdd"
        }
    ))
    adm_no = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '10',
            'placeholder': "Enter borrower's admission number",
            'id': 'admAdd'
        }
    ))
    grade = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'maxlength': '2',
            'placeholder': "Enter borrower's class",
            'id': 'gradeAdd'
        }
    ))
    section = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'maxlength': '1',
            'placeholder': "Enter borrower's section",
            'id': 'sectionAdd'
        }
    ))
    roll_no = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'maxlength': '1',
            'placeholder': "Enter borrower's roll number",
            'id': 'rollAdd'
        }
    ))
    contact_no = forms.IntegerField(widget=forms.TextInput(
        attrs={
            
            'class': 'form-control',
            'minlength': '-9223372036854775808',
            'maxlength': '9223372036854775807',
            'placeholder': "Enter borrower's contact number",
            'id': 'contactAdd'
        }
    ))

    book_borrowed = forms.CharField(widget=forms.TextInput(
        attrs={
            
            'class': 'form-control',
            'placeholder': "Search Book's Title",
            'id': 'bookBorrowedAdd', 
            'autocomplete': 'off', 
            'type': 'text', 
            'onkeyup':"dynamicSearchForAdd();displaySearchElemsForAdd()", 
            'title' : "Type in a name"

        }
    ))
    
    date_borrowed = forms.DateField(widget=forms.DateInput(
        attrs={
            
            'class': 'form-control',
            'type':'date', 
            'placeholder': "Enter date borrowed",
            'id': 'dateBorrowedAdd', 
         
        }
    ))

    date_due = forms.DateField(widget=forms.DateInput(
        attrs={
            
            'class': 'form-control',
            'type':'date', 
            'placeholder': "Enter date due: ",
            'id': 'dateDueAdd', 
         
        }
    ))
    
    
class DeleteBorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = '__all__'
    pk = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'style': 'display: none',
            'id': "primaryKeyDel"
        }
    ))
    