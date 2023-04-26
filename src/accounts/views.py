from django.shortcuts import render
from django.contrib.auth.models import User

from django.views.generic import CreateView

from .forms import SignupForm

from django.urls import reverse_lazy 

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')
