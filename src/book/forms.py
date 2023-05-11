from django import forms 
from .models import Book, Review


class BookForm(forms.ModelForm):
    class Meta:    
        model = Book
        fields = ('bookname', 'subtitle', 'text','thumbnail', 'category')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("text", "rate")
        
# class SearchForm(forms.ModelForm):
#     bookname = forms.CharField(required=False)
    
#     class Meta:
#         model = Book
        