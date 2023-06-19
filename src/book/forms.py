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
        labels={
           'text':'コメント',
           'rate':'評価',
           }

    
class BookNameSearch(forms.ModelForm):
    bookname = forms.CharField(label='', max_length=50,required=False)

    class Meta:
        model = Book
        fields = ('bookname',)
        
class SubtitleSearch(forms.ModelForm):
    subtitle = forms.CharField(label='', max_length=50,required=False)
    class Meta:
        model = Book
        fields = ('subtitle',)