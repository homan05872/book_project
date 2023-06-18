from django.contrib.auth.forms import UserCreationForm
from book.models import Profiel
from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()

from allauth.account.forms import SignupForm,LoginForm
from allauth.account.adapter import DefaultAccountAdapter

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'

class CustomSignupForm(SignupForm): #SignupFormを継承する
    nickname = forms.CharField(max_length=30, label='ニックネーム')
    
    def signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # here you can change the fields
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['nickname'].widget.attrs['class'] = 'form-control'
        self.fields['nickname'].widget.attrs['placeholder'] = 'ニックネーム'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',"nickname") 
        
class ProfielUpdateForm(forms.ModelForm):
    class Meta:
        model = Profiel
        fields = ('nickname', 'text', 'sex', 'img')