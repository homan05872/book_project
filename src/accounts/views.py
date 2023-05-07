from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.views.generic import CreateView

from .forms import SignupForm, Profielform

from django.urls import reverse_lazy 

from book.models import Profiel

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')
    

def profiel_new(request):
    if request.method == "POST":
        form = Profielform(request.POST)
        if form.is_valid:
            profiel = form.save(commit=False)
            profiel.outher = request.user
            profiel.save()
            return redirect('booklist')
    else:
        form = Profielform()
    return render(request,'profiel/profiel_new.html',{'form':form})

