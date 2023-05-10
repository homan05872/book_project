from django.forms import ModelForm 
from .models import Book, Review


class BookForm(ModelForm):
    class Meta:    
        model = Book
        fields = ('bookname', 'subtitle', 'text','thumbnail', 'category')


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ("text", "rate")