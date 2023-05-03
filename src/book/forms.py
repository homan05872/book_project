from django import forms
from .models import Book


class Bookform(forms.ModelForm):
    model = Book
    fields = ('title', 'text', 'category')
