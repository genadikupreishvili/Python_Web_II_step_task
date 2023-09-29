
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import CustomUser, Book, Author, Genre, Condition




class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    genre = forms.ModelChoiceField(queryset=Genre.objects.all())
    condition = forms.ModelChoiceField(queryset=Condition.objects.all())

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'condition', 'location', 'description']



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number')

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class ConditionForm(forms.ModelForm):
    class Meta:
        model = Condition
        fields = ['description']
