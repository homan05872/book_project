from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from book.models import Profiel
from django import forms

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',) 
        
class Profielform(forms.ModelForm):
    class Meta:
        model = Profiel
        fields = ('nickname','text','sex')